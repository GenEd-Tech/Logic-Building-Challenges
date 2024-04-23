## \python program for calculating Total resistance of parallel resistors\

def parallel_resistance(resistances): # function to calculate the total resistance
    return 1 / sum(1 / r for r in resistances)
    
List_of_resistors=[] # list of all resistance values

try:
    number_of_resistors = int(input("Enter No. of resistor: ")) #input for number of resistors

    for i in range(number_of_resistors): 
        enter_resistance_values=int(input(f"Enter_resistance value for resistor number {i+1} :"))
        List_of_resistors.append(enter_resistance_values)  # append all values to the list
        
        
    total_resistance = parallel_resistance(List_of_resistors)

    print("Total resistance:" , round(total_resistance,2), "ohms")

except ValueError:
    print("Invalid Input")


