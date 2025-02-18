# WeChatAI 开发者指南

## 项目概述
本项目的目标是通过集成开源AI模型和微信自动化工具，构建一个可对话的微信机器人。

## 环境配置
### 系统要求
- Python 3.8+
- Windows 10/11 或 Linux/macOS（需已安装微信）

### 快速安装
```bash
git clone https://github.com/yourname/WeChatAI
cd WeChatAI
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
模型部署
下载 ChatGLM3-6B 模型：
huggingface-cli download --resume-download THUDM/chatglm3-6b --local-dir model/chatglm3-6b



配置文件
参数说明
参数	值示例	作用
MODEL_DIR	./model/chatglm3-6b	本地模型路径
WECHAT_LISTEN_LIST	["family_group"]	监听群聊名称
USE_4BIT_QUANT	True	开启内存优化模式

开发流程
调试模式
python src/bot.py --debug
支持图片回复
def handle_image(self, img_path):
    self.wx.SendFiles(img_path)
测试指南
python -m pytest tests/


常见问题
Q1: 微信无法连接
✅ 确认微信客户端已登录且窗口可见
✅ 运行前关闭杀毒软件防止拦截
Q2: 生成回复速度慢
⚡️ 开启 USE_4BIT_QUANT = True 降低内存占用
⚡️ 设置 WECHAT_REPLY_DELAY = 0 禁用模拟延迟
---

### **附加工具脚本**

#### **安装依赖脚本 (`scripts/install_deps.ps1`)**
```powershell
# Windows PowerShell 专用
python -m pip install --upgrade pip
pip install torch==2.1.0 transformers==4.36.0 -i https://mirror.sjtu.edu.cn/pytorch-wheels/torch/
pip install -r ../requirements.txt

运行验证
初始化数据库
mkdir -p data && python -c "from database import init_db; init_db()"

启动程序
python src/bot.py
此项目框架遵循模块化设计原则，可轻松扩展功能。建议开发者根据实际需求调整模型参数或添加新的消息处理逻辑


WeChatAI/
├── docs/
│   ├── DEVELOPER_GUIDE.md    # 开发者文档（见下文）
│   └── CHANGELOG.md          # 版本更新日志（预留）
├── src/
│   ├── bot.py                # 主程序
│   ├── config.py             # 配置文件
│   ├── database.py           # 数据库操作
│   ├── training/
│   │   ├── train.py          # 模型训练
│   │   └── utils.py          # 训练工具函数
│   └── model/
│       └── chatglm3-6b/      # 本地模型存储目录
├── logs/                     # 日志目录
├── data/
│   └── chat_history.db       # 数据库文件
├── scripts/
│   ├── install_deps.ps1      # 一键安装依赖脚本（Windows）
│   └── setup_env.sh          # 环境初始化（Linux/macOS）
├── requirements.txt          # 依赖清单
└── README.md                 # 用户指南
















