#!/bin/bash
# 简单的预览脚本 - 使用 Python 内置服务器

PORT=8000

# 检查 Python 是否安装
if ! command -v python3 &> /dev/null; then
    echo "❌ 错误：未找到 Python3，请先安装 Python"
    exit 1
fi

# 检查 index.html 是否存在
if [ ! -f "index.html" ]; then
    echo "❌ 错误：找不到 index.html 文件"
    exit 1
fi

echo "🚀 启动预览服务器..."
echo "📱 访问地址: http://localhost:$PORT/index.html"
echo "💡 按 Ctrl+C 停止服务器"
echo ""

# 在后台打开浏览器（macOS）
sleep 1 && open "http://localhost:$PORT/index.html" 2>/dev/null &

# 启动 Python 服务器
python3 -m http.server $PORT

