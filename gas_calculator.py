# calculate the cost to fill up a car's gas tank based on the price of gas and the size of the tank
import math 

fuel_tank_size = float(input("Enter fuel tank size in gallons: "))

price = float(input("Enter price of gas ($/gallon): "))

remaining_fuel_amount = float(input("Enter starting fuel amount(in gallons): "))


# Subtract remaining fuel amount from tank size (difference), then take difference and 
# multiply by price
def calculate():
    
    difference = fuel_tank_size - remaining_fuel_amount

    cost = price * difference

    rounded_cost = math.ceil(cost * 100) / 100 

    print("Cost to fill tank: $" ,rounded_cost)

calculate()