import requests
from bs4 import BeautifulSoup as bs

def getHtml(url):
    try:
        kv={"user-agent":"Mozilla/5.0"}
        r=requests.get(url,headers=kv,timeout=30)
        r.raise_for_status
        r.encoding=r.apparent_encoding
        print(r.text)
    except:
        print('Error')

if __name__=="__main__":
    url='http://www.baidu.com'
    getHtml(url)
