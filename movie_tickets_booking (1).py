

'''
age=int(input())
if age<5:
    print("free")
elif age>=5 and age<=12:
    print("child ticket:",100)
elif age>= 13 and age<=59:
    print("regular ticket:",200)
else:
    print("Senoir citizen ticket:",120)'''

'''
=int(input())
if n>0:
    print("Positive number")
elif n<0:
    print("Negative number")
else:
    print("zero")'''

'''
day=str(input())
if day == "saturday" or day == "sunday":
    print("Discount Applicable")
else:
    print("No discount")'''

'''
Tickets = int(input())
if Tickets<=6:
    print("Bookng allowed")
else:
    print("Booking limited accessed")'''


'''
n=int(input())
box=24
fbox=n//24
rchoco=n%24
print(f"{fbox} full boxes,{rchoco} leftover")


dis=int(input())   #km
mileage=int(input())  #km/l
fcost=int(input())
mil=dis/mileage
fc=mil*fcost
print("total fuel cost:",fc)


salary=int(input())
hra=salary*20/100
da= salary*10/100
print(salary+hra+da)'''




#mohan did code
def login_system():
    a=input("Enter user id: ")
    b=input("Enter passwad: ")
    if a=="admin" and b=="admin@123":
        print("login accessed")
    else:
        print("deny access")
        login_system()
    print("--------------------------------------------------")
    selection_of_move()
                                                                                  

def selection_of_move():
    print('''Avalable moves:
1.DC
2.spirit
3.husharu pitalu
4.god father
5.run''')
    move=input("Enter a movie name:").lower()
    if move == "dc" or "spirit" or "husharupitalu" or "god father" or "run":
        print("move is avalable")
    else:
        print("move is not avalble")
    print("--------------------------------------------------")
    ticket_price()

def ticket_price():
        print("1.balcany(150 rupes) ,2.narmal(100 rupes)")
        a=input("Enter the palce:")
        if a == "balcany":
            global ticket
            ticket=150
            print("ticket price :150")
        else:
            ticket=100
            print("ticket price :100")
        print("--------------------------------------------------")   
        tickets_booking_allowed_or_not()

def tickets_booking_allowed_or_not():
    Tickets = int(input("Enter number of Tickets:"))
    if Tickets<=6:
        global number_tickets
        number_tickets=Tickets
        print("Bookng allowed")
        discount_applicable_or_not()
    else:
        print("Booking limit exceeded")
        tickets_booking_allowed_or_not()        
    print("--------------------------------------------------")
    


def discount_applicable_or_not():
    day=str(input("Enter a week name for discount:"))
    if day == "saturday" or day == "sunday":
        print("Discount Applicable 10%")
        price=(ticket*number_tickets)
        discount=price*0.1
        total=price-discount
        print(f'{number_tickets}*{ticket}:',price)
        print("discount price",discount)
        print("total price:",total)
    else:
        print("No discount")
        price=(ticket*number_tickets)
        print("total rpice",price)
    

    

'''age=int(input())
if age<5:
    print("free")
elif age>=5 and age<=12:
    print("child ticket:",100)
elif age>= 13 and age<=59:
    print("regular ticket:",200)
else:
    print("Senoir citizen ticket:",120)'''


#18-08-2026
'''a=float(input())
b=float(input())
c=float(input())
d=float(input())
volume=b-c
space=d-a
if volume==0:
    print(0)
elif space<=0:
    print(-1)
else:
    print(space/volume)'''

'''a=input()
if a=="red":
    print("Stop")
elif a=="yellow":
    print("Ready to go")
else:
    print("Invalied signal color")'''
   

'''
a=int(input())
b=int(input())
c=int(input())

if a==b and a==c:
    print("all are same")
elif (a==b and a!=c) or (a!=b and a==c):
    print("only two numbers are same")
else:
    print("All defferent")
    '''

'''f=int(input())
a=f//100
b=(f//10)%10
c=f%10
if a==b and a==c:
    print("all are same")
elif (a==b and a!=c) or (a!=b and a==c):
    print("only two numbers are same")
else:
    print("All defferent")'''

#match case
'''n=int(input())
match n:
    case 1:
        print("sunday")
    case 2:
        print("Monday")
    case 3:
        print("Tuesday")
    case 4:
        print("wedsday")
    case 5:
        print("thusday")
    case 6:
        print("friday")
    case 7:
        print("saterday")
    case _:
        print("not valied")'''


'''markes=float(input())
if markes>35:
    if markes>75:
        print("distention")
    else:
        print("pass")
else:
    print("fail")'''

'''
a=input("Enter user id: ")
b=input("Enter passwad: ")
if a=="admin":
    if b=="admin@123":
        print("login accessed")
    else:
        print("Passwad is wrong")
        print("deny access")
elif a!="admin" and b!="admin@123":
    print("user id and passwad is wrong")
    print("deny access")
else:
    print("user id  is wrong")
    print("deny access")'''       


login_system()











