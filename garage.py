class Parking_Garage():                                 

    def __init__(self):
        self.tickets = [1,2,3,4,5,6,7,8,9,10] #Tickets available
        self.spaces = [1,2,3,4,5,6,7,8,9,10]  #Spaces available                                                                                                                                                 
        

    def park(self):   #Takes ticket
        if self.tickets == 0:
            print("\nYou have rented out every space!")
        else:
            self.tickets.pop(0)  #Decrease amount of available tickets
            self.spaces.pop(0)   #Decrease amount of spaces   
            current_ticket['owned'] += 1                                                                                                                                       
            current_ticket['paid'] = False
            print(f"\nYou have taken {current_ticket['owned']} ticket(s), their are {len(self.tickets)} tickets left.")

    def pay(self):     #Pay for parking                                                                      
        if current_ticket['paid'] == True:
            print("\nYou have paid your ticket, you have the space for 15 minutes. ")
        elif current_ticket['paid'] == False:
            pays = int(input("\nEnter how many tickets you would like to pay for: "))
            current_ticket['owned'] -= pays
            self.tickets.append(0)
            self.spaces.append(0) 
            if pays >= current_ticket['owned']:
                current_ticket['paid'] = True
                print("Thank you, you have paid for all of your tickets and have 15 minutes to leave.")
            else:
                print(f"You have paid for {pays} ticket(s) and still have {current_ticket['owned']} ticket(s) to pay for!")                                                                                             
        elif current_ticket['paid'] == None:
            print("\nYou have not taken a ticket. ")

    def leave(self):
        if current_ticket['paid'] == False:
            print(f"\nYou have {len(current_ticket)} ticket(s) to pay for!")
            self.pay()
        elif current_ticket['paid'] == True:
            print("\nGoodbye!")
        

def run():
    while True:
        option = input("Would you like to pay, park, or leave? ")
        if option == 'park':
            my_tix.park()
        elif option == 'pay':
            my_tix.pay()
        elif option == 'leave':
            my_tix.leave()
        


current_ticket = {'paid': None, 'owned': 0}                                #Need to add owned tickets and wether or not they have been paid for

my_tix = Parking_Garage()
run()


