
#Vending Machine 

#Student Name: Syed Muslim Mehdi
#CS Year 1 

#1: Create Products lists, Every product has its own identity code, name and a price.
products = {
    "Z1" : ["Popcorn", 2.50],
    "Z2" : ["Strawberry Juice", 4.00],
    "Z3" : ["Cookies", 8.00],
    "Z4" : ["Red Bull", 12.00],
    "M1" : ["Water", 1.00],
    "M2" : ["CupCake", 3.50],
    "M3" : ["Slice Cake", 2.00],
    "G1" : ["Milk", 4.00],
    "G2" : ["Soda", 2.50],
    "G3" : ["Pepsi", 2.00],
    "G4" : ["Dew", 3.50],
    "A1" : ["Fanta", 5.00],
    "A2" : ["7UP", 2.50],
    "A3" : ["Galaxy", 3.50],
    "A4" : ["Doritos", 3.00],
    "Q1" : ["M&m", 4.00],
    "Q2" : ["Skittles", 3.50],
    "Q3" : ["Glucose Biscuit", 1.00],
    "Q4" : ["Nuts", 1.50],

}



#2: In the second step we will code welcome message.
def welcome_message_():

    print("Welcome to Mehdi Vending Machine!!!") 
    print("You can buy your favourite Snacks & Drinks here!")
    print("Kindly follow the guidelines provided below!")
    print()

#This function displays a welcome message to the users and explains the purpose of vending machine, To improve realiyability, A single line.


#3: In this step we will display the product menu.
def show_products_():
    print("Amoung are the products available: ")     
    for code, details in products.items(): 
        print(f"{code}: {details[0]} - aed{details[1]:.2f}: " ) 
        print()
        
        
#This funtion provides a list of every item that is offered in vending machine, To improve realiyability, A single line.


#4: Funtion to get the consumers selected product.
def choose_product():
    while True: 
        code = input("insert the product code: ").upper()  #Input to upercase.
        if code in products: 
            return code
        else: 
            print("The product code you have entered is incorrect please enter a correct product code!")

#Enables the user to enter a product unique code to choose it. Make sures that the product code is correct or incorrect.

#5: Payment handeling function.
def payment_process(cost): 
    print(f"The cost of the product is aed{cost:.2f}. please insert money." )
    total_inserted = 0.0  
    while total_inserted < cost: 
            try:
                money = float (input(f"Insert money (remaining: aed{cost - total_inserted: })"))
                if money > 0 :
                    total_inserted += money

                else: 
                    print("please enter a positive number")
                
            except ValueError:
                print("incorrect input, enter a valid number")
            return total_inserted
            
#This manages the payment system, make sures that consumer have enough money to purchase product.


#6: Calculate and return change funtion.
def calculate_change(total_inserted, cost):
    change = total_inserted - cost
    print(f"Thank you for your purchase, Here is your remaining balance {change:.2f}aed. see you soon!")


#Calculates the total and return the remaining balance.



#8: Main vening machine program.
def vending_machine():
    #Call the welcome message from funtion.
    welcome_message_()

    #Display the availabe products.
    show_products_()

    #Get the selected product code from the use.
    choosen_code = choose_product()

    #use the retrieve products name and price from the dictionary using code.
    product_name, product_price = products[choosen_code]

    #Notify user what the selected.
    print(f"You selected {product_name}, which cost aed {product_price:.2f} ")

    #Process of payment.
    total_inserted = payment_process(product_price)

    #Calculte total and remaining funds.
    calculate_change(total_inserted, product_price)


vending_machine()
















                             

                
     
    











