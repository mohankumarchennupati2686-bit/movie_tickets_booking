def login_system():
    while True:
        a = input("Enter user id: ")
        b = input("Enter password: ")
        if a == "admin" and b == "admin@123":
            print("Login accessed")
            print("-" * 50)
            break
        else:
            print("Access denied. Please try again.")

def selection_of_movie():
    available_movies = ["dc", "spirit", "husharu pitalu", "god father", "run"]
    print('''Available movies:
1. DC
2. Spirit
3. Husharu Pitalu
4. God Father
5. Run''')
    
    while True:
        movie = input("Enter a movie name: ").lower()
        if movie in available_movies:
            print("Movie is available")
            print("-" * 50)
            break
        else:
            print("Movie is not available. Please try again.")

def ticket_price():
    print("1. Balcony (150 rupees) | 2. Normal (100 rupees)")
    place = input("Enter the place (balcony/normal): ").lower()
    if place == "balcony":
        ticket = 150
        print("Ticket price: 150")
    else:
        ticket = 100
        print("Ticket price: 100")
    print("-" * 50)
    return ticket

def tickets_booking_allowed_or_not():
    while True:
        try:
            tickets = int(input("Enter number of tickets: "))
            if tickets <= 6:
                print("Booking allowed")
                print("-" * 50)
                return tickets
            else:
                print("Booking limit exceeded (Maximum 6). Please try again.")
        except ValueError:
            print("Please enter a valid number.")

def discount_applicable_or_not(ticket, number_tickets):
    day = input("Enter a week day name for discount: ").lower().strip()
    price = ticket * number_tickets
    
    if day == "saturday" or day == "sunday":
        print("Discount Applicable 10%")
        discount = price * 0.1
        total = price - discount
        print(f'{number_tickets} * {ticket} = {price}')
        print("Discount amount:", discount)
        print("Total price:", total)
    else:
        print("No discount")
        print("Total price:", price)

# Main execution flow
def main():
    login_system()
    selection_of_movie()
    ticket = ticket_price()
    number_tickets = tickets_booking_allowed_or_not()
    discount_applicable_or_not(ticket, number_tickets)

main()
