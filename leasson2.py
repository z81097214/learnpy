import requests
from lxml import etree

with open("文档.txt","a",encoding="utf-8") as f:
    for i in range(1):
        url="https://www.g58luoli.info/forum-70-{}.html".format(i)
        #url = "https://music.douban.com/top250?start={}".format(i * 25)
        headers = {"User_Agent": "Mozilla/5.0(compatible; MSIE 5.5; Windows 10)"}
        a1=requests.get(url, headers=headers)
        data = a1.text
        # print(a1.status_code)
        # print(a1.encoding)
        # print(a1.text)
        s=etree.HTML(data)
        print(type(s))

        #歌曲整体的XPTH
        musics=s.xpath('//*[@id="normalthread_11124610"]/tr[1]/th/a[2]/text()')
        print(musics[0].strip())
        r1text=musics[0].strip()
        print(type(r1text))
