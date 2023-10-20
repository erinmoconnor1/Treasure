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
choice1 = input("Which door would you like to open? Type one, two, or three. Choose carefully!\n").lower()
if choice1 == "one":
  choice2 = input("Where will your journey to the find the treasure take you next? Left  or Right \n").lower()
  if choice2 == "left":
    choice3 = input("You have stumbled upon a map that tells you to turn around now, will you continue on your treasure hunt on turn around? Type continue or turn around.\n").lower()
    if choice3 == "continue":
      choice4 = input("You have come across a lagoon. Will you try to swim or use the boat sitting on the shore? Type swim or boat.\n").lower()
      if choice4 == "boat":
        print("You used the boat to cross the lagoon and found the Treasure on the other side!")
      else:
        print("The lagoon was full of hungry sharks and you were eaten!")
    else:
      print("You turned around and fell into a pit of venomous snakes and died!")
  else:
    print("No! You took the wrong turn and got lost! You were never seen again!")
else:
  print("Wrong Door! You were eaten by a pack of wild monkeys!")

  