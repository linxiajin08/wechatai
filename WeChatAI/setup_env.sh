#!/bin/bash
# 一键环境初始化脚本

set -e  # 遇到错误立即退出

# 检测是否国内网络
check_in_china() {
    curl -s --connect-timeout 3 http://www.google.com &> /dev/null || return 0
    return 1
}

# 设置镜像源
if check_in_china; then
    echo "⚡ 检测到国内网络，使用清华镜像源加速"
    export PIP_INDEX_URL=https://pypi.tuna.tsinghua.edu.cn/simple
    export HF_ENDPOINT=https://hf-mirror.com
fi

# 安装系统依赖（Debian/Ubuntu）
if command -v apt-get &> /dev/null; then
    sudo apt-get update
    sudo apt-get install -y python3-dev python3-venv
fi

# 创建并激活虚拟环境
python3 -m venv .venv
source .venv/bin/activate

# 安装PyTorch
if nvidia-smi &> /dev/null; then
    echo "✅ 检测到CUDA环境，安装GPU版PyTorch"
    pip install torch==2.1.0 torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
else
    echo "⚠️  使用CPU版PyTorch"
    pip install torch==2.1.0 torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
fi

# 安装其他依赖
pip install -r ../requirements.txt

echo -e "\n🎉 环境配置完成！执行以下命令启动："
echo "source .venv/bin/activate && python src/bot.py"
