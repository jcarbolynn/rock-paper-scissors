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
game_images = [rock, paper, scissors]

player = int(input("Let's play rock, paper, scissors. Type '0' for rock, '1' for paper, or '2' for scissors. "))
if player >= 3 or player < 0:
  print("You typed an invalid number, you lose!")
else:
    
  computer = random.randint(0,2)
  print(f"Computer chose: {computer}\n")
  print(game_images[computer])
  
  
  if player == 0 and computer == 2:
    print("You won!")
  elif computer == 0 and player == 2:
    print("You lost")
  elif computer < player:
    print("You won!")
  elif computer > player:
    print("You lost")
  elif computer == player:
    print("it's a draw!")
