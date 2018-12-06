from urllib import request

class Spider():
    url = 'https://www.douyu.com/g_wzry'
    def __fetch_content(self):
        r = request.urlopen(Spider.url)
        htmls = r.read()
        htmls = str(htmls,encoding='utf-8')
    def go(self):
        self.__fetch_content()
spider = Spider()
spider.go()