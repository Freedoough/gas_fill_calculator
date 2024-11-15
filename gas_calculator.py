# calculate the cost to fill up a car's gas tank based on the price of gas and the size of the tank
import math 
import sys
import time

def percentage_fuel():
   while True:
   # prompt for fuel tank size
    # prompt for percentage of gas in tank
        print("Fuel Calculator (%):\n")






def gallons_remaining():
    #prompt for tank size in gallons
    # prompt for remaining fuel in gallons
    print("gallons remaining")

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