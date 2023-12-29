import random

rock = '''
    rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    paper
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

user_choice = int(input("Type a number - Rock[0], Paper[1], Scissors[2]: "))

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
else:
    print("You chose:")
    print(game_images[user_choice])

    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[computer_choice])

    if (user_choice == 0 and computer_choice == 2) or (user_choice > computer_choice):
        print("You win!")
    elif (computer_choice == 0
          and user_choice == 2) or (computer_choice > user_choice):
        print("You lose!")
    elif computer_choice == user_choice:
        print("It's a draw!")
