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

#Write your code below this line 👇
user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors "))
computer = random.randint(0, 2)

if user >= 3 or user < 0:
    print("You chose an invalid number.")
elif user == 0:
    print(rock)

    print("Computer chose: ")

    if computer == 0:
        print(rock)
        print("It's a tie")
    elif computer == 1:
        print(paper)
        print("You lose")
    else:
        print(scissors)
        print("You win")
elif user == 1:
    print(paper)

    print("Computer chose: ")

    if computer == 0:
        print(rock)
        print("You win")
    elif computer == 1:
        print(paper)
        print("It's a tie")
    else:
        print(scissors)
        print("You lose")
else:
    print(scissors)
    
    print("Computer chose: ")

    if computer == 0:
        print(rock)
        print("You lose")
    elif computer == 1:
        print(paper)
        print("You win")
    else:
        print(scissors)
        print("It's a tie")
