print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
choice_1 = input("You're at a crossroad. Where do you want to go? Type 'left' or 'right'\n")
choice_1 = choice_1.lower()
if choice_1 == "Left".lower():
  choice_2 = input("Your've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.\n")
  choice_2 = choice_2.lower()
  if choice_2.lower() == "Wait".lower():
    choice_3 = input("You arrive the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do youchoose?\n")
    choice_3 = choice_3.lower()
    if choice_3.lower() == "Yellow".lower():
      print("You Win!")
    elif choice_3.lower() == "Blue".lower():
      print("Eaten by beasts.\n Game Over.")
    elif choice_3.lower() == "Red".lower():
      print("Burned by fire.\n Game Over.")
    else:
      print("Game Over")
  else:
    print("Attacked by trout.\n Game Over.")
else:
  print("Fall into a hole\n Game Over.")
