seriesEndNum = int(input("How many Terms do you want?"))

#Recursion Function
def fibonacci(num):
    """
    A recursive function to calculate the Fibonacci sequence.
    
    Parameters:
    - num: an integer representing the position in the Fibonacci sequence
    
    Returns:
    - The value at the given position in the Fibonacci sequence
    """
    if num in [0 , 1]:
        return num
    return fibonacci(num-1) + fibonacci(num-2)

fibSeries = [fibonacci(num) for num in range(seriesEndNum)] #list comprehension

# fibSeries = []
# for num in range(seriesEndNum):
#     fibSeries.append(fibonacci(num))

print(fibSeries)