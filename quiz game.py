print("All the praise for almighty Allah".title())
print('Wellcome to my python quiz!'.title())
wish = input("Do you want to play? ")
#jumping on the quiz

if wish.lower() == 'yes':
    print("Let's jump in!")
else:
    quit("okay, see you next time!")

Mark = 0



while True:           #ques-1:
    ques1 = input("Q-1: When Bangladesh got indipendent? ")
    if ques1 == "1971":
        Mark += 1
        print(F"Right Answer! Get ready for the next one!")
        break
    else:
        print(f"Wrong! Let's try again!")

while True:          #ques-2:
    ques2 = input("Q-2: Who designed the national flag of Bangladesh? ")
    if ques2.lower() == "kamrul":
        Mark +=1
        print(F"Right Answer! Get ready for the next one!")
        break
    else:
        print(f"Wrong! Let's try again!")


while True:          #ques-3:
    ques3 = input("Q-3: What is the capital of Bangladesh? ")
    if ques3.lower() == "dhaka":
        Mark +=1
        print(F"Right Answer! Get ready for the next one!")
        break
    else:
        print(f"Wrong! Let's try again!")

while True:          #ques-4:
    ques4 = input("Q-4: What are the official language of Bangladesh? ")
    if ques4.lower() == "bangla":
        Mark +=1
        print(F"Right Answer! Get ready for the next one!")
        break
    else:
        print(f"Wrong! Let's try again!")


while True:          #ques-5:
    ques5 = input("Q-5: How many districts are there in Bangladesh? ")
    if ques5.lower() == "64":
        Mark +=1
        print(F"Right Answer! Get ready for the next one!")
        break
    else:
        print(f"Wrong! Let's try again!")
print(f"congratulations! You have answred all the questions! You have obtain {Mark} marks!")










