# _*_ coding:utf-8 _*_


# 这里我统计的是我的ACM模板的所有C++代码,当然也有个别的Java代码,没有统计
# 这里也只是粗算,没有详细计算, 没有处理注释符在字符串里的情况

from pathlib import Path 

def solve(fileUrl):
    p = Path(fileUrl)
    FileList = list(p.rglob('*.cc')) # 当前目录下的所有.jpg文件的路径
    # 遍历每个文件
    cnt_line = 0
    cnt_empty = 0
    cnt_note = 0
    text = ''
    for File in FileList:
        with open(File,'r',encoding='UTF-8') as f:
            text = f.read()
        # print(text)
        texts = text.split('\n')
        cnt_line = cnt_line + len(texts)
        nt = False
        for line in texts:
            if line == '':
                cnt_empty = cnt_empty + 1
            
            if '/*' in line or nt:
                cnt_note = cnt_note + 1
                nt = True
                if '*/' in line:
                    nt = False
            for c in line:
    cnt_line = cnt_line - cnt_empty - cnt_note
    print('I writed {} lines code'.format(cnt_line))
    print('I writed {} lines empty line'.format(cnt_empty))
    print('I writed {} lines note'.format(cnt_note))

if __name__ == '__main__':
    solve('F:/CPC/template')
