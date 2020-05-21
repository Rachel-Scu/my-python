#获取淘宝商品名称和价格
import requests
from bs4 import BeautifulSoup
import re

def getHTMLText(url):  
    try:
        kv={'cookie':'cna=W5EhF7EVNmcCAXr05OXn02Qt; _m_h5_tk=fce425eb1194a5a695fefcbb20d79fae_1587455324193; _m_h5_tk_enc=3c1d23085684b8048db14af5da4d50c7; lLtC1_=1; miid=1776832934939621204; _samesite_flag_=true; cookie2=10a4e5849c373ea4b7f27a98051d7117; t=e1badc81253a9c462ff6d7a9545514c8; _tb_token_=733e463535356; tk_trace=oTRxOWSBNwn9dPyorMJE%2FoPdY8zfvmw%2Fq5hp2qO3VMDgFSCVRzUQ3TlRAADZUcMqkJnRqcepw0XUEViBsJB8Z%2BpYECchBq%2B5CCVegoj0jKJ3SwV6ruMROMwz0843qDeuJGIllSm3soEa3TKrMU22EFaqiKjF8J2CA2P5x66hAZDABp42kI%2B5rFLOIpQB3yqTny%2BseqG6ohRE5swd1mS8zg7u6XEr45l7ASlehDQJ4W0eVcQSFFzDzvOdR3OxkssLHi4UGK6VQ2XSR3je0l7dDFl%2FqRaM; v=0; hng=CN%7Czh-CN%7CCNY%7C156; thw=cn; sgcookie=EmxKhjXs%2B8ildKCf0LD5k; unb=2206513712563; uc3=id2=UUphzOff%2BpQeAD9xCA%3D%3D&nk2=F5RMEYFeReZWzuc%3D&lg2=W5iHLLyFOGW7aA%3D%3D&vt3=F8dBxGR3%2BZ48pPMD63c%3D; csg=508e86fa; lgc=tb983901169; cookie17=UUphzOff%2BpQeAD9xCA%3D%3D; dnk=tb983901169; skt=f5419bbf66eb97f1; existShop=MTU4NzQ0ODM0Nw%3D%3D; uc4=id4=0%40U2grF8wSV9PAXe85Cqxrhqt%2FBPL4tuMq&nk4=0%40FY4HVFrFYFk3JVMPcviTzbJ1bvRAOA%3D%3D; tracknick=tb983901169; _cc_=U%2BGCWk%2F7og%3D%3D; _l_g_=Ug%3D%3D; sg=93c; _nk_=tb983901169; cookie1=VAMQDjxoTyca49%2FCJUDuhAI%2FzB8NuIBcXnRPAOApqqw%3D; tfstk=cX5NBmts15FaN7NdeCd25WST7cpOaC9DUX8vIToAV0obuSvM4sYKDe4IDe8J2WvG.; enc=d8lr5Cz7dQ4W5LmDD6FmJaM043q6V9GMMLktE%2BPQZzD7k9uxtx95zRq6E9cBfMJqRyCbpEZFU%2FDyXwJ55OiCgMp5W9CCR3W%2FZfsLqZJXmIY%3D; uc1=cookie16=VT5L2FSpNgq6fDudInPRgavC%2BQ%3D%3D&cookie21=V32FPkk%2FgPzW&cookie15=Vq8l%2BKCLz3%2F65A%3D%3D&existShop=false&pas=0&cookie14=UoTUPcilbR%2FTJQ%3D%3D; mt=ci=0_1; l=eBEbiylPQ2Bv4lHDBOfiRqkF6E_9DIRfguk28DMwiT5P9616iDZhWZXE9yTBCnGVn6WXR3JE6OGwB58EhyUCNxv9-eTCgsDKFdBG.; isg=BOjoQ6FZIhVMlQ6R1wwawhGoudb6EUwbjaNWdqIZR2PJ_YlnSiCpq4n38ZUNTQTz; JSESSIONID=A95BA2685C0039A8831ACBF2E20B2BD8',
            "user-agent":"Mozilla/5.0"}
        r=requests.get(url,headers=kv,timeout=30)
        r.raise_for_status
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return " "

def parsePage(ilt,html):
    soup=BeautifulSoup(html,"html.parser")
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)
        tlt = re.findall(r'\"raw_title\"\:\".*?\"',html)
        for i in range(len(plt)):
            price=eval(plt[i].split(':')[1])
            title=eval(tlt[i].split(':')[1])
            ilt.append([price,title])
    except:
        print(" ")

def printGoodsList(ilt):
    tplt="{0:^4}\t{:^8}\t{:^6}"
    print(tplt.format("序号","价格","商品名称"))
    count=0
    for g in ilt:
        count=count+1
        print(tplt.format(count,g[0],g[1]))
    print("")
    
def main():
    goods="书包"
    depth=2
    start_url='http://s.taobao.com/search?q='+goods
    infoList=[]
    for i in range(depth):
        try:
            url=start_url+'&s='+str(44*i)
            html=getHTMLText(url)
            parsePage(infoList,html)
        except:
            continue
    printGoodsList(infoList)

if __name__=="__main__":
    main()