# calculate the cost to fill up a car's gas tank based on the price of gas and the size of the tank
import math 
import sys
import time

def percentage_fuel():
   while True:
   # prompt for fuel tank size
    # prompt for percentage of gas in tank
        print("Fuel Calculator (%):\n")

        choice = str(input("Menu:\n (1): Continue to calculator\n (2): Switch Calculation\n (3): Exit Program\n> ").rstrip())

        if choice == "1":
            try:
                tank_size = int(input("Enter fuel tank size (gallons): ").rstrip())
                percentage = float(input("Enter the approximate percentage of fuel in your tank (decimal form): ").rstrip())
                gas_price = float(input("Enter price of gas (USD $): ").rstrip())

                percent_to_whole_num_difference = tank_size * percentage

                tank_size_difference = tank_size - percent_to_whole_num_difference 

                price_to_fill = gas_price * tank_size_difference

                rounded_cost = math.ceil(price_to_fill * 100) / 100

                print(f"Cost to fill tank: $ {rounded_cost}")

               
            except ValueError:
                print("INVALID input, please enter percentage in decimal form (i.e. .25 for 25%)")
                          

        elif choice == "2":
            print("Switching calculation\n")
            time.sleep(1)
            return
        elif choice == "3":
            print("Exiting Program")
            sys.exit()
        else:
            print("INVALID\n")
            time.sleep(2)

def gallons_remaining():
    #prompt for tank size in gallons
    # prompt for remaining fuel in gallons
    while True:

        print("Fuel Calculator (gallons remaining): \n")

        choice = str(input("Menu:\n (1): Continue to calculator\n (2): Switch Calculation\n (3): Exit Program\n> ").rstrip())

        if choice == "1":
            try:
                tank_size = int(input("Enter fuel tank size (gallons): ").rstrip())
                remaining_fuel = float(input("Enter remaining fuel (gallons): ").rstrip())
                gas_price = float(input("Enter price of gas (USD $): ").rstrip())
                
                tank_difference = tank_size - remaining_fuel

                fuel_cost = tank_difference * gas_price

                rounded_cost = math.ceil(fuel_cost * 100) / 100

                print(f"Cost to fill tank: $ {rounded_cost}")
            except ValueError:
                print("INVALID input, please enter numeric value.")

        elif choice == "2":
            print("Switching calculation\n")
            time.sleep(1)
        elif choice == "3":
            print("Exiting Program")
            sys.exit()
        else:
            print("INVALID\n")
            time.sleep(2)        

def get_info():

    while True:
        type = str(input("Calculate:\n (1): Percentage of fuel remaining\n (2): Gallons remaining\n (3): Exit Program\n> ").rstrip())

        if type == "1":
            percentage_fuel()
        elif type == "2":
            gallons_remaining()
        elif type == "3":
            print("Exiting Program")
            sys.exit()
        else:
            print("INVALID\n")
            time.sleep(1)


get_info()

# OLD CODE



# fuel_tank_size = float(input("Enter fuel tank size in gallons: "))

# price = float(input("Enter price of gas ($/gallon): "))

# remaining_fuel_amount = float(input("Enter starting fuel amount(in gallons): "))


# # Subtract remaining fuel amount from tank size (difference), then take difference and 
# # multiply by price
# def calculate():
    
#     difference = fuel_tank_size - remaining_fuel_amount

#     cost = price * difference

#     rounded_cost = math.ceil(cost * 100) / 100 

#     print("Cost to fill tank: $" ,rounded_cost)

# calculate()