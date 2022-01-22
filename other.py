# Add card and Zip limit
# Add extra option for Other AKA sexy time!
# Add loop into adding money if you dont have enough cash
# or call police
# Fix case sensetive dumb ass
# Add how much is left over they owe
# if no to card loop into MILITARY DEATH BY FIRE SQUAD!
# add in : after card and zip code dumb ass
# storage for people in parking garage
# idea== name's or digits into list?
# after we owe you send to customer service chat?
import time
class Parking_Garage():
    def __init__(self):
        self.tickets = ['1','1','1','1','1','1','1','1','1','1']
        self.spaces = ['1','1','1','1','1','1','1','1','1','1']
        self.currentticket = {}
        self.takeTicket()
    def takeTicket(self):
        response = input("Would you like to take a ticket? ")
        if response != 'yes' and response != 'no':
            print("Enter yes or no ")
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
        time_parked = int(input("How long did you stay? "))
        cost = time_parked * 20
        print("Give me " + str(cost) + " money now hoe!")
        paymenttype = input("What type of payment would you like to use? Cash, Card or favor? ")
        if paymenttype == 'cash':
            payment = int(input("How much are you paying? " ))
            print("Insert Cash")
            time.sleep(0.2)
            print('Processing')
            time.sleep(2)
            if payment == cost:
                self.currentticket['paid'] = True
                print("Thank you")
                self.leave()
            if payment > cost:
                self.currentticket['paid'] = True
                change = payment - cost
                print(f"We owe you {change}")
                self.leave
            if payment < cost:
                self.currentticket['paid'] = False
                print("Pay me hoe")
                self.pay()
        if paymenttype == 'card':
            print("We gonna charge more boiiii")
            going = input("Want that charge yes or no ")
            if going == 'yes':
                card = input('Whats your card number? ')
                time.sleep(0.5)
                zip = input('Enter ZipCode ')
                time.sleep(0.5)
                print('Taking all your money bruh!....')
                time.sleep(0.8)
                self.currentticket['paid'] = True
                self.leave()
    def leave(self):
        if self.currentticket['paid'] == True:
            print("Thank you, we didn't enjoy your buisness!")
            self.tickets.append('1')
            self.spaces.append('1')
myticket = Parking_Garage()
