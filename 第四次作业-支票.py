import turtle
def main():
    name=GetName()
    hour_pay=GetHour_pay()
    working_hours=GetWorking_hours()
    total_pay=TotalPay(hour_pay,working_hours)
    IntName(name,total_pay)
    
def GetName():
    return input("Please enter the name:")

def GetHour_pay():
    return float(input("Please enter the hour pay:"))

def GetWorking_hours():
    return int(input("Please enter the working hour:"))

def TotalPay(hour_pay,working_hours):
    if working_hours<=40:
        return hour_pay*working_hours
    else:
        fisr_part=hour_pay*40
        second_part=1.5*hour_pay*(working_hours-40)
        return fisr_part+second_part

def IntName(name,total_pay):
    Backgound()
    #add name
    turtle.pencolor("black")
    turtle.penup()
    turtle.goto(-250,100)
    turtle.pendown()
    turtle.write(name,font=("Arial" ,14 , "bold"))
    #add money1
    turtle.penup()
    turtle.goto(-250,40)
    turtle.pendown()
    turtle.write('$ '+format(total_pay,'.2f'),font=("Arial" ,18 , "bold"))
    #add money2
    turtle.penup()
    turtle.goto(260,45)
    turtle.pendown()
    turtle.write(format(total_pay,'.2f'),font=("Arial" ,12 , "bold"))
    turtle.hideturtle()

def Backgound():
    turtle.speed(0)
    turtle.bgcolor('lightblue1')
    turtle.setup(720,480)
    #line one
    turtle.penup()
    turtle.goto(-340,160)
    turtle.pendown()
    turtle.write("citi",font=("Arial" , 30 , "bold"))
    turtle.penup()
    turtle.goto(-280,160)
    turtle.pendown()
    turtle.write("bank",font=("Arial" , 30 , "normal"))
    turtle.penup()
    turtle.goto(-175,162)
    turtle.pendown()
    turtle.pencolor("dark slate grey")
    turtle.write("Citibank (Hong Kong) Limited",font=("Arial" ,16 , "normal"))
    turtle.penup()
    turtle.goto(180,165)
    turtle.pendown()
    turtle.write("月Month     日Day    年Year",font=("Arial" ,8 , "normal"))
    turtle.goto(340,165)
    #line two
    turtle.penup()
    turtle.goto(-340,100)
    turtle.pendown()
    turtle.pencolor("grey")
    turtle.write("祈付",font=("Arial" ,8 , "normal"))
    turtle.goto(-260,100)
    turtle.pendown()
    turtle.goto(290,100)
    turtle.write("或持票人",font=("Arial" ,8 , "normal"))
    turtle.goto(340,100)
    turtle.goto(340,130)
    #line three
    turtle.penup()
    turtle.goto(-340,40)
    turtle.pendown()
    turtle.pencolor("grey")
    turtle.write("港元",font=("Arial" ,8 , "normal"))
    turtle.goto(200,40)
    turtle.goto(200,70)
    turtle.penup()
    turtle.goto(215,45)
    turtle.pencolor("dark slate grey")
    turtle.write("HK  $",font=("Arial" ,12 , "bold"))
    #line four
    turtle.penup()
    turtle.goto(-340,-20)
    turtle.pendown()
    turtle.pencolor("grey")
    turtle.goto(140,-20)
    turtle.goto(140,10)
    turtle.penup()
    turtle.goto(180,0)
    turtle.pendown()
    turtle.pencolor("purple")
    turtle.write("For and on behalf of",font=("Arial Nova" ,10 , "italic"))
    turtle.penup()
    turtle.goto(180,-20)
    turtle.pendown()
    turtle.write("paydollar.com",font=("Arial Nova" ,16 , "normal"))
    turtle.penup()
    turtle.goto(180,-60)
    turtle.pendown()
    turtle.write(".......................................................")
    turtle.penup()
    turtle.goto(200,-70)
    turtle.pendown()
    turtle.write("Authorized Signature(s)",font=("Arial Nova" ,8 , "normal"))
    #line five
    turtle.penup()
    turtle.goto(-340,-60)
    turtle.pendown()
    turtle.pencolor("dark slate grey")
    turtle.write("ASIAPAY HK LTD TRADING AS",font=("Arial" ,12 , "normal"))
    turtle.penup()
    turtle.goto(-340,-80)
    turtle.pendown()
    turtle.write("PAYDOLLAR.COM",font=("Arial" ,12 , "normal"))

if __name__=='__main__':   
    main()
    Backgound()
