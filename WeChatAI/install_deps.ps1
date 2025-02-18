<#
.SYNOPSIS
一键安装项目依赖（Windows PowerShell）
支持自动检测CUDA并安装对应版本的PyTorch
#>

# 错误时终止执行
$ErrorActionPreference = "Stop"

# 检查CUDA可用性
$hasCuda = $false
try {
    $cudaInfo = nvidia-smi --query --display=COMPUTE | Select-String "CUDA Version"
    if ($cudaInfo) {
        Write-Host "✅ 检测到CUDA环境" -ForegroundColor Green
        $hasCuda = $true
    }
} catch {
    Write-Host "⚠️  未检测到NVIDIA驱动，将安装CPU版本PyTorch" -ForegroundColor Yellow
}

# 安装PyTorch
if ($hasCuda) {
    Write-Host "正在安装CUDA 12.1版PyTorch..." -ForegroundColor Cyan
    pip install torch==2.1.0 torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
} else {
    Write-Host "正在安装CPU版PyTorch..." -ForegroundColor Cyan
    pip install torch==2.1.0 torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
}

# 安装其他依赖（使用清华源加速）
Write-Host "安装其他依赖项..." -ForegroundColor Cyan
pip install -r ..\requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

# 完成提示
Write-Host "`n🎉 依赖安装成功！请运行 'python src\bot.py' 启动项目" -ForegroundColor Green
