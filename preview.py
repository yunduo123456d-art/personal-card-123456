#!/usr/bin/env python3
"""
简单的本地预览服务器
运行后会在浏览器中自动打开预览页面
"""

import http.server
import socketserver
import webbrowser
import os
import sys

PORT = 8000

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        super().end_headers()

def main():
    # 切换到脚本所在目录
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    # 检查 index.html 是否存在
    if not os.path.exists('index.html'):
        print("❌ 错误：找不到 index.html 文件")
        sys.exit(1)
    
    Handler = MyHTTPRequestHandler
    
    try:
        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            url = f"http://localhost:{PORT}/index.html"
            print(f"🚀 预览服务器已启动")
            print(f"📱 访问地址: {url}")
            print(f"💡 按 Ctrl+C 停止服务器\n")
            
            # 自动在浏览器中打开
            try:
                webbrowser.open(url)
                print("✅ 已在浏览器中打开预览页面\n")
            except:
                print("⚠️  无法自动打开浏览器，请手动访问上述地址\n")
            
            # 启动服务器
            httpd.serve_forever()
            
    except OSError as e:
        if e.errno == 48:  # Address already in use
            print(f"❌ 端口 {PORT} 已被占用，请关闭其他服务或修改端口号")
        else:
            print(f"❌ 启动服务器时出错: {e}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n\n👋 预览服务器已停止")
        sys.exit(0)

if __name__ == "__main__":
    main()

