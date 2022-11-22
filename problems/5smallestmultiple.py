# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?



def smallestMultiple():

    counter = 0
    number = 1

    while number < 10000:
        for i in range(1, 20): # Loop through all 1..20
            if number % i == 0: # If our number has no remainder
                counter += 1
            elif number % i == 1:
                break
        
        if counter == 20: # All values from 1..20 have no remainder
            return number
        
        number += 1
        counter = 0
                


print(smallestMultiple())