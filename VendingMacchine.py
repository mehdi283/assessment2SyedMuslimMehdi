#Vending Machine 

#Student Name: Syed muslim mehdi
#CS Year 1 

#1: Create Products lists, Every product has its own identity code, name and a price.

products = {
    "Z1" : ["Popcorn", 2.50],
    "Z2" : ["Chocolate", 4.00],
    "Z3" : ["Cookies", 2.00],
    "Z4" : ["Energy Drink", 5.00],
    "M1" : ["Water", 1.00],
    "M2" : ["CupCake", 3.50],
    "M3" : ["juice", 2.00],
    "G1" : ["Milk", 4.00],
    "G2" : ["Soda", 2.50],
    "G3" : ["Ice Cream", 3.00],
    "G4" : ["Nuts", 1.50],

#Products code, name, price list.
}



#2: In the second step we will code welcome message.

def welcome_message_():
    print("Welcome to Mehdi Vending Machine!!!")
    print("You can buy your favourite Snacks & Drinks here!")
    print("Kindly follow the guidelines provided below!")
#This function gives the user a welcome message and some basic guidence
    
    print()

#To improve realiyability, A single line.


#3: In this step we will display the product menu.

def show_products_():
    #This funtion provides a list of every item that is offered in vending machine.
    print("Amoung are the products available: ")
    for code, details in products.item(): 
        print(f"{code}: {details[0]} - aed{details[1]}: " ) 

        print()
        #To improve realiyability, A single line.

#4: Funtion to get the consumers selected product.

def choose_product():
#By inputting the product code, the user can choose products using this funtion. 

     while True: 
        code = input("insert the product code: ").upper()  #Input to upercase.
        if code in products: 

            return code
            
        else: 
            print("The product code you have entered is incorrect please enter a correct product code!")
            

#5: Payment handeling function.

def payment_process(cost):
    #This funtion manages money insertion and make sure the customer insert an enough amount to buy products.
    print(f"The cost of the product is aed{cost: }. please insert money." )
    total_inserted = 0.0   #Calculate money inserted by the consumers.
    while total_inserted < cost: #Keep asking for funds untill enough fund is added.
            try:
                #This funtion asks user to pay.
                money = float (input(f"Insert money (remaining: aed{cost - total_inserted: })"))
                if money > 0 :

                 total_inserted += money

                else: 
                    print("please enter a positive number")
                
            except ValueError:
                print("incorrect input, enter a valid number")

                return total_inserted
            









                
                                                    

                
     
    











