#Learning the input function

#Parrot function, ends using break
def Parrot():
    prompt = "\nTell me something and I will say it back to you,"
    second = " \nor enter quit: "
    combined = prompt+second
    message = ''
    while True:
        message = input(combined)
        if message != 'quit':
            print (message)
        else:
            print ("The parrot flew away!")
            break
        
        

#Even or Odd
def Even_or_odd():
    number = input('Give me a number: ')
    number = int(number)
    if number % 2 == 0:
        print(f'{number} is Even!\n')
    else:
        print(f'{number} is Odd!\n')