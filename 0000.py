# -*- coding: utf-8 -*-

'''
参考链接 https://blog.csdn.net/smallcolzacio/article/details/78285334
'''

from PIL import Image, ImageDraw, ImageFont

def add_num(img):
    # 创建一个Draw对象
    draw = ImageDraw.Draw(img)
    # 创建一个Font
    myfront = ImageFont.truetype('C:/windows/fonts/Arial.ttf', size = 40)
    # 填充的颜色
    fillcolor = '#ff0000' 
    # 图像对象的宽高
    width, height = img.size
    # 在Draw对象上画
    draw.text((width-80,0),'+50',font = myfront,fill=fillcolor)
    img.save('result.jpg','jpeg')

if __name__ == "__main__":
    # 创建图像对象
    image = Image.open('image.jpg')
    add_num(image)
    print('program end!')