import sys # module containing exit functionality.
import random # module that helps to generate numbers

print("")
playerchoice = int(input("Enter...\n1 for Rock,\n2 for Paper, or \n3 for Scissor:\n\n"))


if playerchoice < 1 | playerchoice > 3:
  sys.exit("You must enter 1, 2, or 3.")

computerchoice = int(random.choice("123")) # selects a random integer from string "123"

if (playerchoice == 1):
  print("You choose Rock.")
elif (playerchoice == 2):
  print("You choose Paper.")
elif (playerchoice == 3):
  print("You choose Scissor.")

if (computerchoice == 1):
  print("Python choose Rock.")
elif (computerchoice == 2):
  print("Python choose Paper.")
elif (computerchoice == 3):
  print("Python choose Scissor.")

if (computerchoice == 1 and playerchoice == 1) or (computerchoice == 2 and playerchoice == 2) or (computerchoice == 3 and playerchoice == 3):
  print("It's a tie")
elif (playerchoice == 1 and computerchoice ==3) or (playerchoice == 2 and computerchoice == 1) or (playerchoice == 3 and computerchoice == 2):
  print("You win! Hurray!")
else:
  print("Computer wins.")
