# 
'''
激活码 Activation Code
产生200个激活码
'''
import random

def get_code(n,length = 20):
    # 字符集合
    list = [] 
    # 在list加入0-9
    for i in range(10):
        list.append(str(i))
    
    # 在list中加入'A'-'Z'
    for i in range(65,91):
        list.append(chr(i))
    
    # 在list中加入'a'-'z'
    for i in range(97,123):
        list.append(chr(i))
    
    # for c in list:
    #     print(c)
    ans = []

    for i in range(200):
        # 在list集合中随机选择length个字符 并返回一个list
        myslice = random.sample(list, length) 
        # 将list变成一个字符串
        veri_code = ''.join(myslice)
        ans.append(veri_code)
    return ans

if __name__ == '__main__':
    list = get_code(200)
    for lis in list:
        print(lis)
    print('program end')
