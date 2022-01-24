class Parking_Garage():                                 

    def __init__(self):
        self.tickets = [1,2,3,4,5,6,7,8,9,10] #Tickets available
        self.spaces = [1,2,3,4,5,6,7,8,9,10]  #Spaces available                                                                                                                                                 
        

    def park(self):   #Takes ticket
        if len(self.tickets) == 0:
            print("\nYou have rented out every space!")
        else: #Decrease amount of tickets/spaces, add to owned tickets
            self.tickets.pop(0) 
            self.spaces.pop(0)  
            current_ticket['owned'] += 1                                                                                                                       
            current_ticket['paid'] = False #Since new tickets are held, you cant leave
            print(f"\nYou have taken {current_ticket['owned']} ticket(s), their are {len(self.tickets)} tickets left.")

    def pay(self): #Pay for parking                                                                      
        if current_ticket['paid'] == True:
            print("\nYou have paid your ticket, you have the space for 15 minutes. ")
        elif current_ticket['paid'] == False:
            print(f"\nYou have taken {current_ticket['owned']} ticket(s), their are {len(self.tickets)} tickets left.")
            pays = int(input("\nEnter how many tickets you would like to pay for: "))
            for num in range(pays): #Loop that cycles through adding the amount of held tickets to lists, and taking away from owned tickets
                self.tickets.append(current_ticket['owned']) 
                self.spaces.append(current_ticket['owned'])
                current_ticket['owned'] -= 1 
            if pays >= current_ticket['owned']: #Must pay for the amount of tickets you hold
                current_ticket['paid'] = True
                print("Thank you, you have paid for all of your tickets and have 15 minutes to leave.") 
            else:
                print(f"You have paid for {pays} ticket(s) and still have {current_ticket['owned']} ticket(s) to pay for!")                                                                                             
        elif current_ticket['paid'] == None:
            print("\nYou have not taken a ticket. ")

    def leave(self):
        if current_ticket['paid'] == False:
            print(f"\nYou have {len(current_ticket)} ticket(s) to pay for!")
            self.pay() #Prompts you to go back and pay for a ticket
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
        


current_ticket = {'paid': None, 'owned': 0}                                

my_tix = Parking_Garage()
run()


