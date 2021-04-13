import random
x = ["head", "tails"]
y = input("heads or tails? ")

if y == random.choice(x):
  print("Congo you have won the toss")
elif y != random.choice(x):
  print("you have lost the toss")
else:
  print("choose a valid option")
