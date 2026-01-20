#!/usr/bin/env python3
"""
生成 PWA 所需的图标文件
需要安装: pip install Pillow cairosvg
或者使用在线工具: https://realfavicongenerator.net/
"""

try:
    from PIL import Image, ImageDraw, ImageFont
    import os
    
    def create_icon(size, filename):
        """创建指定尺寸的图标"""
        # 创建黑色背景
        img = Image.new('RGB', (size, size), color='#000000')
        draw = ImageDraw.Draw(img)
        
        # 绘制一个简单的图标（圆形 + 文字）
        # 绘制圆形
        margin = size // 8
        draw.ellipse([margin, margin, size - margin, size - margin], 
                    fill='#64ff64', outline=None)
        
        # 绘制文字（如果尺寸足够大）
        if size >= 180:
            try:
                # 尝试使用系统字体
                font_size = size // 3
                font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", font_size)
                text = "营"
                # 获取文字尺寸
                bbox = draw.textbbox((0, 0), text, font=font)
                text_width = bbox[2] - bbox[0]
                text_height = bbox[3] - bbox[1]
                # 居中绘制
                position = ((size - text_width) // 2, (size - text_height) // 2 - 10)
                draw.text(position, text, fill='#000000', font=font)
            except:
                # 如果字体加载失败，跳过文字
                pass
        
        # 保存文件
        icons_dir = os.path.join(os.path.dirname(__file__), 'icons')
        os.makedirs(icons_dir, exist_ok=True)
        filepath = os.path.join(icons_dir, filename)
        img.save(filepath, 'PNG')
        print(f"✓ 已创建: {filename} ({size}x{size})")
    
    # 创建所需的图标尺寸
    print("正在生成图标...")
    create_icon(192, 'icon-192.png')
    create_icon(512, 'icon-512.png')
    create_icon(180, 'apple-touch-icon.png')
    create_icon(32, 'favicon.png')
    
    # 复制 32x32 作为 favicon.ico（如果需要）
    from PIL import Image
    favicon = Image.open('icons/favicon.png')
    favicon.save('icons/favicon.ico', format='ICO')
    print("✓ 已创建: favicon.ico")
    
    print("\n所有图标已生成完成！")
    
except ImportError:
    print("""
错误：需要安装 Pillow 库
    
安装方法：
    pip install Pillow
    
或者使用在线工具生成图标：
    1. 访问 https://realfavicongenerator.net/
    2. 上传一个 512x512 的图标
    3. 下载生成的所有图标文件
    4. 将图标文件放到 icons/ 目录下
    """)
