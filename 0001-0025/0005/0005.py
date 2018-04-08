# _*_ coding:utf-8 _*_

from pathlib import Path 
from PIL import Image

def solve(fileUrl):
    p = Path(fileUrl)
    ImgFileList = list(p.glob('*.jpg')) # 当前目录下的所有.jpg文件的路径
    ImgFileList.extend(list(p.glob('*.jpeg'))) # 当前目录下的所有.jpeg文件的路径
    # print(type(ImgFileList))
    # 遍历每个文件
    for imgFile in ImgFileList:
        # print(type(imgFile))
        img = Image.open(imgFile) # 打开文件
        if max(img.size) > 1136: # 如果文件最大尺寸大于1136 则修改
            value = max(img.size) / 1136.0
            newsize_min = min(img.size) / value
            newimg = img.resize((1136,int(newsize_min)),Image.ANTIALIAS) # 文件的resize处理
            newimg.save('new_'+imgFile.name,'jpeg') # 保存文件
        else: # 如果分辨率不大于1136 则不用处理
            print('This picture is availabe: ' + imgFile.name)

if __name__ == '__main__':
    solve('F:\photo2')
