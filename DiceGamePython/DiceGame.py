""" Phase One: 
Create a dice game where a user can guess what no. the dice will land on

"""
import random

dice_input = int(input("Guess a number from 1 to 6 for our first round of rolling a dice" ))

print(dice_input)

numberGenerated = random.randint(1,6)
print (numberGenerated)

def diceGame ():
  if dice_input < numberGenerated:
    print("Your guess is less than the answer")
  elif dice_input > numberGenerated:
    print("Your guess is greater than the answer")  
  else:
    print("Your guess is correct! Congratulations! Let's move to the next round!")

diceGame()
