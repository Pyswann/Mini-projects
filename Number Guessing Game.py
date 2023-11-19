


import random
cnumber = random.randint(0,10)
gNumber = int(input("Enter your number:  "))
while cnumber != gNumber:
    print("!!!Wrong guess!!!")
    if cnumber > gNumber:
        print("You number is short than the computer number")
        gNumber = int(input("Enter your number again:  "))
    elif gNumber > cnumber:
        print("You number is big than the computer number")
        gNumber = int(input("Enter your number again:  "))
    else:
        break
print("Boyaah! You guess the right answer!")





























