'''
1 for snake
-1 for water
0 for gun
'''
# import random
# # computer = -1# we want random choise from  computer that why we use import random 
# computer = random.choice([-1,0,1]) 
# youstr = (input("Enter your choice: "))
# youdict = {
#     "s":1, "w":-1,"g":0}
# reversedict = {
#     1:"snake",-1:"water",0:"gun"}
# you = youdict[youstr]
# print(f"you chose {reversedict[you]}\n Computer chose {reversedict[computer]}")
# if (computer ==you):
#     print("IT IS A DRAW")
# else:
#     if(computer ==-1 and you ==1):
#         print("YOU WIN")
#     elif(computer ==-1 and you ==0):
#         print("YOU LOSE")
#     elif(computer ==1 and you ==-1):
#         print("YOU LOSE")
#     elif(computer ==1 and you == 0):
#         print("YOU WIN")
#     elif(computer ==0 and you ==-1):
#         print("YOU WIN")
#     elif(computer ==0 and you ==1):
#         print("YOU LOSE")
#     else:
#         print("SOME THING WENT WROGN")



#NEW  ADD 
# import random
# '''
# 1 for snake
# -1 for water 
# 0 for gun
# '''
# computer = random.choice([-1, 0, 1])
# youstr = input("Enter your choice: ")
# youDict = {"s": 1, "w": -1, "g": 0}
# reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

# you = youDict[youstr]

# # By now we have 2 numbers (variables), you and computer

# print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

# if(computer == you):
#     print("Its a draw")

# else:
#     '''
#     if(computer ==-1 and you == 1): (computer - you) = -2
#         print("You win!")

#     elif(computer ==-1 and you == 0): (computer - you) = -1
#         print("You Lose!")

#     elif(computer == 1 and you == -1): (computer - you) = 2
#         print("You lose!")

#     elif(computer ==1 and you == 0): (computer - you) = 1
#         print("You Win!")

#     elif(computer ==0 and you == -1): (computer - you) = 1
#         print("You Win!")

#     elif(computer == 0 and you == 1): computer - you) = -1
#         print("You Lose!") 

#         The below logic is written on the basis of the value of computer - you

#     '''
#     if((computer - you) == -1 or  (computer - you) == 2 ):
#         print("You lose!")
#     else:
#         print("You win!") 

