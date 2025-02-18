class Config:
    """全局配置参数"""
    # ========== 微信配置 ==========
    WECHAT_LISTEN_LIST = ["family_group"]         # 监听的群聊名称或好友备注
    WECHAT_REPLY_DELAY = 2.0                      # 模拟回复延迟（秒）
    
    # ========== 模型配置 ==========
    MODEL_NAME = "THUDM/chatglm3-6b"              # 使用 ChatGLM-6B 模型
    MODEL_DIR = "./model/chatglm3-6b"             # 本地模型路径
    USE_4BIT_QUANT = True                         # 启用4-bit量化
    
    # ========== 训练配置 ==========
    TRAIN_EPOCHS = 1                              # 训练周期
    TRAIN_LEARNING_RATE = 3e-5                    # 学习率
    LOAD_IN_8BIT = False                          # 是否用8-bit加速
    
class PathConfig:
    """路径配置"""
    LOG_DIR = "./logs"
    DB_PATH = "./data/chat_history.db"
