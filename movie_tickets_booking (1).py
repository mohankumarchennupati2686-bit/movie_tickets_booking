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


login_system()











