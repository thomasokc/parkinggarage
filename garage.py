class Parking_Garage():
    def __init__(self):
        self.tickets = [10]
        self.spaces = ['1','2','4,','5','6','7','8','9','10']
        self.currentticket = {}
        self.takeTicket()

    def takeTicket(self):
        response = input("Would you like to take a ticket?")
        if response != 'yes' and response != 'no':
            print("Enter yes or no")
            self.takeTicket()
        if response == 'yes':
            if len(self.spaces) > 0:
                self.spaces.pop()
                self.tickets.pop()
                self.pay()
            else:
                print("We are full")
        if response == 'no':
            print("Come back")

    def pay(self):
        paymenttype = input("What method of payment would you like to use? Cash or Card?")
        cost = 1
        if paymenttype == 'cash':
            payment = int(input("How much are you paying?"))
            print("Insert Cash")
            if payment >= cost:
                self.currentticket['paid'] = True
                print("Thank you")
                self.leave()
        if paymenttype == 'card':
            card = input('Please insert card')
            self.currentticket['paid'] = True
            self.leave()

    def leave(self):
        if self.currentticket['paid'] == True:
            print("Thank you, we didn't enjoy your buisness!")
            self.tickets.append('1')
            self.spaces.append('1')

my_ticket = Parking_Garage
def run():
        while True:
            response = input('Would you like to do? Park, Pay, Leave?').lower()
            if response == 'park':
                my_ticket.takeTicket()
            elif response == 'pay':
                my_ticket.pay
            elif response == 'take':
                my_ticket.leave
while True:
        my_ticket()
        if input("Are you leaving?") !='No':
            break