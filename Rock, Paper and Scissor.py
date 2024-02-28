import random

rock = '''
    ______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''
paper='''
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
game_sign = [rock, paper, scissors]

user_choice = (input("what do you choose? 0 = rock, 1 = paper, 2 = Scissors.\n"))
user_choice = int(user_choice)

if user_choice not in [0, 1, 2]:
   print("you Choice wrong number.")
else:
  print("Your choice:")
  print(game_sign[user_choice])
  
  computer_choice = random.randint(0, 2)
  print("computer choice:")
  print(game_sign[computer_choice])

  if computer_choice == user_choice:
    print("You drop.")
    
  elif (user_choice == 0 and computer_choice == 2) or (user_choice > computer_choice):
      print("You win!")

  elif computer_choice > user_choice:
   print("Computer wins!, You lost.")
