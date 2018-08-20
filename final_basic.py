TICKET_PRICE = 10
SERVICE_CHARGE = 2
tickets_remaining = 100
def calculate_price(ticket_n):
    return (TICKET_PRICE * ticket_n) + SERVICE_CHARGE

while tickets_remaining > 0:
    print("there are {} tickets left".format(tickets_remaining))
    user_name = input("Please input your friggin name:  ")
    no_tickets = input("how many tickets would {} like today?  ".format(user_name))
    #Handle ValueError
    try:
        no_tickets = int(no_tickets)
        if no_tickets > tickets_remaining:
            raise ValueError("Not enough tickets left")
    except ValueError as err:
        print("Invalid value,try again")
        print("{}".format(err))
    else:
        total_price = calculate_price(no_tickets)
        print("That will be {} dollar billas my good sir {}".format(total_price,user_name))
        confirm_order = input("are you sure yn ?")
        if confirm_order.lower() == "y":
            print("Sold!")
            tickets_remaining -= no_tickets
        else:
            print("Thank you for your day {} anyways".format(user_name))
print("We are sold out, bye") 

        