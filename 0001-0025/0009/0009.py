from bs4 import BeautifulSoup

html_doc = '''
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
'''

if __name__ == '__main__':
    soup = BeautifulSoup(html_doc,'lxml') # 如果不加入lxml，会提示错误
    # print(soup.get_text())
    urls = soup.findAll('a')
    print(type(urls))
    for url in urls:
        print(type(url))
        print(url['href'],url['class'],url['id'])
