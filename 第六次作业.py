def GetInfo():
    names=[]
    expens=[]
    again='y'
    while again=='y' or again=='Y':
        name=input("Please enter the name:")
        names.append(name)
        money=float(input("Please enter the money:"))
        expens.append(money)
        print("Do you want to add anothor name?")
        again=input("y/Y=yes n/N=no:")
    return expens,names
def nameOfBestCustomers(sales,customers):
    Max=max(sales)
    res_list=[]
    index=0
    while index < len(sales):
        if sales[index]==Max:
            res_list.append(customers[index])
        index+=1
    return res_list

def main():
    sales,customers=GetInfo()
    print("The best customer:",end="")
    name_list=nameOfBestCustomers(sales,customers)
    index=0
    while index<len(name_list):
        print(name_list[index],end=" ")
        index+=1
if __name__=='__main__':
    main()
