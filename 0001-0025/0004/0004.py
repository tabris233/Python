# _*_ coding:utf-8 _*_
# 这样写 资源消耗太大，最好一行一行的/read(SIZE)读取计算

# 单词提取
def get_words(text):
    words = []
    temp = ''
    for c in text:
        if c.isalpha():
            temp = temp+c
        elif temp.isalpha():
            words.append(temp)
            temp = ''
    return words

# 单词统计
def countWords(words):
    cnt = {}
    for word in words:
        word = word.lower()
        if word in cnt:
            cnt[word] = cnt[word] + 1
        else:
            cnt[word] = 1
    return cnt

if __name__ == '__main__':
    # 打开文件
    with open('F:/Python/practice/0000-0025/0004/0004.txt', 'r',encoding='UTF-8') as f:
        text = f.read()

    # for c in text:
    #     print(c)
    # print(text)

    words = get_words(text)
    
    cnt = countWords(words)

    # print(len(cnt))
    # for ct in cnt:
    #     print(ct, cnt[ct])

    with open('F:/Python/practice/0000-0025/0004/0004-output.txt','w+',encoding='UTF-8') as f:
        for ct in cnt:
            f.write(str(ct) + ': ' + str(cnt[ct]) + '\n') # f.write 仅支持单个字符串
