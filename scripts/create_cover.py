from PIL import Image, ImageDraw, ImageFont
import sys

# 创建 16:9 的图片
width, height = 1920, 1080
img = Image.new('RGB', (width, height), color='#2563EB')

# 添加文字
draw = ImageDraw.Draw(img)
text = "Claude Code\n让 AI 成为你的编程搭档"

# 尝试使用系统字体
try:
    font = ImageFont.truetype("/System/Library/Fonts/PingFang.ttc", 80)
except:
    font = ImageFont.load_default()

# 计算文字位置（居中）
bbox = draw.textbbox((0, 0), text, font=font)
text_width = bbox[2] - bbox[0]
text_height = bbox[3] - bbox[1]
position = ((width - text_width) // 2, (height - text_height) // 2)

# 绘制文字
draw.text(position, text, fill='white', font=font, align='center')

# 保存
img.save('cover.png')
print("封面图已创建: cover.png")
