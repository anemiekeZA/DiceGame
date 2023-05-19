"""Phase two:
Allow the user to guess the result of two dices being rolled.

"""
import random

dices = []
nums = []

for round in range(1,3):
  dice = int(input("Guess a number from 1 - 6 for round " + str(round)+ "\n"))
  dices.append(dice)

  numberGenerated = random.randint(1,6)
  nums.append(numberGenerated)

  print ("Our Number is", str(numberGenerated))

  if dice < numberGenerated:    
    print("Your guess is less than the answer")
  elif dice > numberGenerated:
    print("Your guess is greater than the answer")  
  else:
    print("Your guess is correct! Congratulations! Let's move to the next round!")

numsTotal = 0
for num in nums:
  numsTotal += num

dicesTotal = 0
for dice in dices:
  dicesTotal += dice

print ("Our Total is: ", str(numsTotal) + "\nYour guess was: "+ str(dicesTotal))


# nums = [5, 4] 
# nums.append(numberGenerated)

# dices = [3, 2]
# dices.append(dice)


# thingsToAddUp = [nums, dices] # [[5, 4], [ 3, 2]]
# totalThings = []
# for thing in thingsToAddUp:
#   currentTotal = 0
#   for i in thing:
#     currentTotal += i
#   totalThings.append(currentTotal)

# print(numsTotal)
# print(dicesTotal)
# print(totalThings)

# numsTotal = numsTotal + i
# numsTotal = 0 + 5
# numsTotal = 5 + 4

  # dice = int(input("Guess a number from 1 - 6 for our second dice " ))
  
  # print("our Number is", str(numberGeneratedSecRound))

# dice = int(input("Lets see if your two guesses made up our final dice number " ))

# numGen = numberGenerated + numberGenerated









