import requests
import os

def getPic(url):
    root="C:/users/rachel/desktop/"
    path=root+url.split('/')[-1]
    try:
        if not os.path.exists(root):
            os.mkdir(root)
        if not os.path.exists(path):
            kv={'user-agent':'Moziila/5.0'}
            r=requests.get(url,headers=kv,timeout=30)
            with open(path,'wb') as f:
                f.write(r.content)
                print("文件成功保存")
        else:
            print("文件已存在")
    except:
        print("爬取失败")
if __name__=="__main__":
    url="https://zimg.zazhimall.com.cn/images/201811/source_img/7076_P_1542849040566.jpg"
    getPic(url)