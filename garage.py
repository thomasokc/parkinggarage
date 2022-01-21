import time

class Parking_Garage():

    def __init__(self):
        self.spaces = ['1','2','4,','5','6','7','8','9','10']
        self.currentticket = {}
        self.takeTicket()

    def takeTicket(self):
        response = input("Would you like to take a ticket?")
        if response != 'yes' and response != 'no':
            print("Enter yes or no")
            self.takeTicket()
        if response == 'yes':
            if len(self.parkingspaces) > 0:
                self.parkingspaces.pop()
                self.tickets.pop()
                self.PayforParking()
            else:
                print("We are full")
        if response == 'no':
            print("Come back")

    def pay(self):
        pass

    def leave(self):

def run():
    while True:
        response = input('Would you like to do? Park, Pay, Leave?').lower()
        if response == 'park':
            my_ticket.takeTicket()
        elif response == 'pay':
            my_ticket.pay
        elif response == 'take':
            my_ticket.leave




my_ticket = Parking_Garage()
run()



