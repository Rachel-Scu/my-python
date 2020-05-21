str=input("请输入一个单词：")
res=[]
for i in range(len(str)):
    for j in range(len(str)-i):
        res.append(str[j:j+i+1])
print(res)     
