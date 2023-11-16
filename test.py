# answer = '123'
# ques =input('what is ur pass? ')
# if ques != answer:
#     print("wrong")
# else:
#     print("correct")









# if user_name.lower() == unam and password == key:
#     print("Great work")
# else:
#     print("incorrect user name and password")

unam = 'al amin'
key = 1234
# demo-2
# while True:
#     user_name = str(input("enter user name: "))
#     password = int(input("enter password: "))
#     if user_name.lower() == unam and password == key:
#         print("congo")
#         break
#     else:
#         print('incorrect')



# demo-3:
# print("demo-3")
# while True:
#     user_name = str(input("enter user name: "))
#     password = int(input("enter password: "))
#     if user_name.lower() != unam or password != key:
#         print("incorrect")
#         break
#     else:
#         print('congo')

# demo-4:
print("demo-4")
while True:
    user_name = str(input("enter user name: "))
    password = int(input("enter password: "))
    if not(user_name.lower() != unam and password != key):
        print("congo")
        break
    else:
        print('incorrect')


