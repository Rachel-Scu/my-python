import requests
from bs4 import BeautifulSoup

count=0
def getHTMLText(url):
    try:
        kv={"user-agent":"Mozilla/5.0"}
        r=requests.get(url,headers=kv,timeout=30)
        r.raise_for_status
        #r.encoding="utf-8"
        return r.text
    except:
        print("Failed to get HTML!")
        
def getInfoList(html):
    soup=BeautifulSoup(html,"html.parser")
    #获取书名
    bookName=soup.find_all('div',class_='pl2')
    bklist=[]
    for ahref in bookName:
        bookName_a=ahref.find('a')['title']
        bklist.append(bookName_a)
     #print(bklist)
        
     #获取其他信息
        bookElse=soup.find_all('p',class_='pl')
        elist=[]
        for text in bookElse:
            bookElse_t=text.get_text()
            elist.append(bookElse_t)
        #print(elist)

    #获取评分
    bookScore=soup.find_all('span',class_='rating_nums')
    scolist=[]
    for score in bookScore:
        bookScore_s=score.get_text()
        scolist.append(bookScore_s)
    #print(scolist)
        
    #获取评价
        bookRemarks=soup.find_all('span',class_='inq')
        remalist=[]
        for remarks in bookRemarks:
            bookRemarks_r=remarks.get_text()
            remalist.append(bookRemarks_r)
        #print(remalist)
            
    #合并
    All_List=[]
    global count
    for name_,else_,score_,remarks_ in zip(bklist,elist,scolist,remalist):
        count=count+1
        title_="TOP"+str(count)+":"+'\n'
        name_="书名："+name_+'\n'
        else_="基本信息："+else_+'\n'
        score_="评分："+score_+'\n'
        remarks_="评价："+remarks_+'\n'
        All_List.append(title_+name_+else_+score_+remarks_)
    return All_List
        
def printList(list):
    global count
    if(count<=25 or count>225):
        Str=" 豆瓣读书评分 TOP250 榜单 "
        print(Str.center(72,'*'))
    for i in range(len(list)):
        print(list[i])
        
def main():
    Final_List=[]
    start_url="https://book.douban.com/top250?start="
    for i in range(10):
        url=start_url+str(25*i)
        html=getHTMLText(url)
        Final_List=getInfoList(html)
        printList(Final_List)
    print("成功读取全部书籍！")

if __name__=="__main__":
    main()
