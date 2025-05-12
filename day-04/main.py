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
print("Let's play Rock-Paper-Scissors...")
user_choice= int(input("    Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
game_images = [rock,paper,scissors]
computer_choice = random.randint(0,2)

if user_choice == 0:
    print(game_images[user_choice])
    print("Computer Chose: ")
    print(game_images[computer_choice])

    if computer_choice == 0:
        print("It's a Draw!")
    elif computer_choice == 1:
        print("You lose!")
    else:
        print("You win!")

elif user_choice == 1:
    print(game_images[user_choice])
    print("Computer Chose: ")
    print(game_images[computer_choice])

    if computer_choice == 1:
        print("It's a Draw!")
    elif computer_choice == 2:
        print("You lose!")
    else:
        print("You win!")

elif user_choice == 2:
    print(game_images[user_choice])
    print("Computer Chose: ")
    print(game_images[computer_choice])

    if computer_choice == 2:
        print("It's a Draw!")
    elif computer_choice == 0:
        print("You lose!")
    else:
        print("You win!")

else:
    print("You can only choose Rock, Paper or Scissors. Try Again.")


