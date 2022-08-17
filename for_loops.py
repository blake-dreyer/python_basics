#From Python Crash Course - playing with basic loop functions

#Print all numbers 1-20, Must use a for loop

def print_nums():
    numbers = []
    for n in range(1, 21):
        numbers.append(n)
    
    print(numbers)

#Make a list of all numbers from 1 to 1 million then print with a for loop

def million():
    numbers = list(range(1,1000001))
    for n in numbers:
        print(n)

#Make a list from 1 to 1 million, confirm its the correct amount of numbers then return the sum

def million_sum():
    numbers = list(range(1,1000001))
    if min(numbers) == 1 and max(numbers) == 1000000:
        return sum(numbers)
    else:
        return 'Error'

#Make a List of Odd numbers from 1-20

def odds():
    odds = list(range(1,20,2))
    print(odds)





