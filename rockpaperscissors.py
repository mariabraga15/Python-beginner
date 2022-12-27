
#Implementing rock paper and scissors
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
images=[rock,paper,scissors]

user=int(input("What do you want to choose?\n0- for rock, 1-for paper, 2-for scissors \n"))
if user<0 or user>2:
    print("Invalid input! Please put an available option from the list above")
else:
    computer=random.choice(range(3))
    print(f"Your choice: {images[user]}")
    print(f"Computer choice: {images[computer]}")
    
    if(computer==0):
        if user==0:
            print("It's a draw...Play again")
        elif user==1:
            print("You won!")
        else:
            print("You lost!")
    if(computer==1):
        if user==1:
            print("It's a draw...Play again")
        elif user==0:
            print("You lost!")
        else:
            print("You won!")
    if(computer==2):
        if user==0:
            print("You won!") 
        elif user==2:
            print("It's a draw...Play again") 
        else:
            print("You lost!")    
    
    
    




