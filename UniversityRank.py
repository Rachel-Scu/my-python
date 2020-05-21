#2019软科最好中国大学排名
import requests
from bs4 import BeautifulSoup
import bs4

def getHTMLText(url):  
    try:
        kv={"user-agent":"Mozilla/5.0"}
        r=requests.get(url,headers=kv,timeout=30)
        r.raise_for_status
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return " "
#提取信息到列表
def fillUnivList(ulist,html):
    soup=BeautifulSoup(html,"html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr,bs4.element.Tag):
            tds=tr('td')
            ulist.append([tds[0].string,tds[1].string,tds[2].string])

def printUnivList(ulist,num):
    tplt="{0:^10}\t{1:{3}^10}\t{2:^10}"
    print(tplt.format("排名","学校名称","总分",chr(12288)))
    for i in range(num):
        u=ulist[i]
        print(tplt.format(u[0],u[1],u[2],chr(12288)))

def main():
    unifo=[]
    url="http://www.zuihaodaxue.com/zuihaodaxuepaiming2019.html"
    html=getHTMLText(url)
    fillUnivList(unifo,html)
    printUnivList(unifo,20)

if __name__=="__main__":
    main()
