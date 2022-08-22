#Learning the input function

#Parrot
message = input('Tell me something and I will repeat it back to you: ')
print(message)

#Even or Odd
number = input('Give me a number: ')
number = int(number)
if number % 2 == 0:
    print(f'{number} is Even!\n')
else:
    print(f'{number} is Odd!\n')