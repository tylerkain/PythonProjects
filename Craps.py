import random 

def roll_dice():
  die1= random.randrange(1,7)
  die2= random.randrange(1,7)
  return (die1, die2)
def display_dice(dice):
  die1, die2 = dice
  print(f"player rolled {die1} + {die2} = {sum(dice)}")

die_values = roll_dice()
display_dice(die_values)

sum_dice = sum(die_values)

if sum_dice in (7, 11):
  game_status = 'Won'
elif sum_dice in (2,3,12):
  game_status = "Lost"
else:
  game_status = "Continue"
  my_point = sum_dice
  print(f'point is {my_point}')

while game_status == "Continue":
  die_values = roll_dice()
  display_dice(die_values)
  sum_dice = sum(die_values)

if sum_dice == my_point:
  game_status =="Won"
elif sum_dice == 7:
  game_status = "Lost"

if game_status == "Won":
  print("player wins")
else:
  print("player loses")
