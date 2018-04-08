#-*- coding:utf-8-*-  
'''
激活码 Activation Code   插入Redis
'''

import redis  
import string,random  
 
def get_code(n,length=20):
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


def generateCode(n,length=20):  
    r=[]  
    s=string.digits+string.ascii_letters  
    for i in range(n):  
        t=''  
        for j in range(length):  
            t+=random.choice(s)  
        r.append(t)  
    return r  

if __name__ == '__main__':
    # 生成邀请码
    r = generateCode(200)
    for s in r:
        print(s)
    # 存入redis数据库功能
    HOST = 'localhost'
    PORT = 6379
    DB = 15
    rdb = redis.Redis(HOST,PORT,DB)
    for i in range(200):  
        rdb.sadd('Activation Code',r[i])  
    rdb.save()  
    print('program end')
