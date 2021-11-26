import os
import base64
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont

'''
中文推荐和英文推荐分别调用一次函数
'''

def font2pic(fontface,Text='The quick brown fox'):
    
    '''
    根据输入的字体名称和文本，（默认英文文本the quick brown fox）
    在字体库中查找对应字体文件并根据文本内容生成图片，
    最后输出base64
    '''
    
    font_files = './fontfaces/' # 存放字体们的文件夹
    file_end = ['otf','ttf']    # 枚举字体格式
    
    # 判断字体文件是否存在，并获取该字体文件加后缀的字符串
    for i in file_end:  
        font_file= fontface + '.' + i
        if os.path.exists(os.path.join(font_files,font_file)):
            fontFile = font_file
    
    # 绘制图片
    img = Image.new("RGB", (1450, 150), "white")                            # 图片尺寸、背景色
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(os.path.join(font_files,fontFile), size=70)   # 字体路径、字号
    draw.text((50,0), Text, (0,0,0), font=font)                             # 写文本
    
    # 转为base64
    buff = BytesIO()
    img.save(buff, format='PNG')
    img_str = base64.b64encode(buff.getvalue()).decode()
    
    return img_str


def find3fonts(font1, font2, font3, Text='The quick brown fox'):
    
    '''
    输入3个字体和文本，（默认英文文本the quick brown fox）
    返回3个图片
    '''
    
    font1_pic = font2pic(font1, Text)
    font2_pic = font2pic(font2, Text)
    font3_pic = font2pic(font3, Text)
    
    return font1_pic, font2_pic, font3_pic

