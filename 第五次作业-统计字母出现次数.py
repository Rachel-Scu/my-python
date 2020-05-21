count=0
letter_list=[0 for x in range(26)]
rate_list=[0 for x in range(26)]

def Count(letter):
    global count
    if letter>='a' and letter<='z':
        letter_list[ord(letter)-97]=letter_list[ord(letter)-97]+1
        count=count+1
    elif letter>='A' and letter<='Z':
        letter_list[ord(letter)-65]=letter_list[ord(letter)-65]+1
        count=count+1

def Rate():
    global count
    for i in range(26):
        rate_list[i]=letter_list[i]/count*100

def ShowResult():
    for i in range(26):
        if rate_list[i]<1:
            print(chr(65+i)+' <1%',end='\t')
        else:
            print(chr(65+i)+' '+format(rate_list[i],'.0f')+'%',end='\t')
        if (i+1)%4==0:
            print('\n')

def main():
    try:
        with open("input.txt",'r') as fp:
            for line in fp:
                for letter in line:
                    Count(letter)
        Rate()
        ShowResult()
    except Exception as err:
        print(err)

if __name__=='__main__':
    main()
            
            
