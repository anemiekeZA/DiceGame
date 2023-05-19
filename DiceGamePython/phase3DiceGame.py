"""Phase Three:
Allow user to decide how many dices to roll.


"""

import random

#min_range, max_range

def get_num_from_user(message,min_range, max_range):
    
  input_is_numeric = False
  input_in_range = False
  
  while not (input_is_numeric and input_in_range):
    inputFromUser = input(message)
    input_is_numeric = inputFromUser.isnumeric()
    
    if input_is_numeric:
      value = int(inputFromUser)
      input_in_range = value > min_range and value < max_range
      if input_in_range:
        return value
    
    print("Sorry you've entered an incorrect value try again!")
    
guesses = []
nums = []

num_rounds = get_num_from_user("How many rounds do you want to play?",0, 11)

for round in range(1, num_rounds + 1):
  users_guess = get_num_from_user("Guess a number from 1 - 6 for round "+ str(round)+ " of " + str(num_rounds) + "\n" , 0, 7)
#   users_guess = int(input("Guess a number from 1 - 6 for round " + str(round)+ " of " + str(num_rounds) + "\n"))
  guesses.append(users_guess)

  numberGenerated = random.randint(1,6)

  nums.append(numberGenerated)

  print ("Our Number is", str(numberGenerated))

  if users_guess < numberGenerated:    
    print("Your guess is less than the answer")
  elif users_guess > numberGenerated:
    print("Your guess is greater than the answer")  
  else:
    print("Your guess is correct! Congratulations! Let's move to the next round!")

numsTotal = 0
for num in nums:
  numsTotal += num

dicesTotal = 0
for users_guess in guesses:
  dicesTotal += users_guess

print ("Our Total is: ", str(numsTotal) + "\nYour guess was: "+ str(dicesTotal))
