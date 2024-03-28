import string
import random

while True:
    try:
        length = int(input("How long do you want your password to be - "))
        break  
    except ValueError:
        print("Please enter a valid number.")
        
CharsList = string.ascii_letters
NumsList = string.digits

password = ""
for x in range (length):
    randomPosition = random.randint(0, len(CharsList) - 1)
    Uppercase = random.randint(0,1)
    if Uppercase == 1:
        radomNum = random.randint(0, len(NumsList) -1)
        y = CharsList[randomPosition]
        uppercase_char = y.upper()
        password = password + y + str(radomNum)
    else:
        password = password + CharsList[randomPosition]


print(password)
