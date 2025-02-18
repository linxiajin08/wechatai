from wxauto import WeChat
from transformers import AutoModel, AutoTokenizer
from config import Config, PathConfig
from database import ChatMessage
import logging
import time

# 初始化日志
logging.basicConfig(
    filename=f"{PathConfig.LOG_DIR}/app.log",
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s: %(message)s'
)

class WeChatBot:
    def __init__(self):
        self.wx = WeChat()
        self._init_model()
        self._add_listeners()

    def _init_model(self):
        """加载本地模型"""
        self.tokenizer = AutoTokenizer.from_pretrained(
            Config.MODEL_DIR, 
            trust_remote_code=True
        )
        self.model = AutoModel.from_pretrained(
            Config.MODEL_DIR,
            device_map="auto", 
            trust_remote_code=True
        )

    def _add_listeners(self):
        """添加微信监听"""
        for chat_name in Config.WECHAT_LISTEN_LIST:
            self.wx.AddListenChat(who=chat_name)
        logging.info("微信监听已启动")

    def run(self):
        """主循环"""
        while True:
            msgs = self.wx.GetAllMessage()
            for sender, msg in msgs:
                response = self._generate_response(msg)
                self.wx.SendMsg(response, sender)
                self._save_to_db(sender, msg, response)
            time.sleep(1)  # 每隔1秒检查新消息

    def _generate_response(self, text):
        """生成回复"""
        try:
            response, _ = self.model.chat(
                self.tokenizer,
                text,
                history=[],
                max_length=100
            )
            return response
        except Exception as e:
            logging.error(f"模型生成失败: {str(e)}")
            return "AI暂时无法响应"

    def _save_to_db(self, sender, msg, response):
        """持久化存储"""
        from sqlalchemy.orm import sessionmaker
        engine = create_engine(f"sqlite:///{PathConfig.DB_PATH}")
        Session = sessionmaker(bind=engine)
        session = Session()
        try:
            record = ChatMessage(
                sender=sender,
                message=msg,
                response=response
            )
            session.add(record)
            session.commit()
        except Exception as e:
            logging.error(f"保存消息失败: {str(e)}")
        finally:
            session.close()

if __name__ == "__main__":
    bot = WeChatBot()
    bot.run()
