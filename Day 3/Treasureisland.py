print('''*******************************************************************************
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
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************
      ''')
print("Welcome to Treasure Island")
print("Your Mission is to find the treasure.")

def get_choice(prompt, valid_choices):
    while True:
        choice = input(prompt).strip().lower()
        if choice in valid_choices:
            return choice
        print("Invalid choice! Please choose again.")
    
        
def stage_one():
    choice = get_choice("You're at a crossroad. Do you want to go 'left' or 'right'? ", ["left", "right"])
    if choice == "left":
        return True
    print('''
          ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⡀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣤⠀⠀⠀⢀⣴⣿⡶⠀⣾⣿⣿⡿⠟⠛⠁
⠀⠀⠀⠀⠀⠀⣀⣀⣄⣀⠀⠀⠀⠀⣶⣶⣦⠀⠀⠀⠀⣼⣿⣿⡇⠀⣠⣿⣿⣿⠇⣸⣿⣿⣧⣤⠀⠀⠀
⠀⠀⢀⣴⣾⣿⡿⠿⠿⠿⠇⠀⠀⣸⣿⣿⣿⡆⠀⠀⢰⣿⣿⣿⣷⣼⣿⣿⣿⡿⢀⣿⣿⡿⠟⠛⠁⠀⠀
⠀⣴⣿⡿⠋⠁⠀⠀⠀⠀⠀⠀⢠⣿⣿⣹⣿⣿⣿⣿⣿⣿⡏⢻⣿⣿⢿⣿⣿⠃⣼⣿⣯⣤⣴⣶⣿⡤⠀
⣼⣿⠏⠀⣀⣠⣤⣶⣾⣷⠄⣰⣿⣿⡿⠿⠻⣿⣯⣸⣿⡿⠀⠀⠀⠁⣾⣿⡏⢠⣿⣿⠿⠛⠋⠉⠀⠀⠀
⣿⣿⠲⢿⣿⣿⣿⣿⡿⠋⢰⣿⣿⠋⠀⠀⠀⢻⣿⣿⣿⠇⠀⠀⠀⠀⠙⠛⠀⠀⠉⠁⠀⠀⠀⠀⠀⠀⠀
⠹⢿⣷⣶⣿⣿⠿⠋⠀⠀⠈⠙⠃⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠈⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⣴⣶⣦⣤⡀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⣠⡇⢰⣶⣶⣾⡿⠷⣿⣿⣿⡟⠛⣉⣿⣿⣿⠆
⠀⠀⠀⠀⠀⠀⢀⣤⣶⣿⣿⡎⣿⣿⣦⠀⠀⠀⢀⣤⣾⠟⢀⣿⣿⡟⣁⠀⠀⣸⣿⣿⣤⣾⣿⡿⠛⠁⠀
⠀⠀⠀⠀⣠⣾⣿⡿⠛⠉⢿⣦⠘⣿⣿⡆⠀⢠⣾⣿⠋⠀⣼⣿⣿⣿⠿⠷⢠⣿⣿⣿⠿⢻⣿⣧⠀⠀⠀
⠀⠀⠀⣴⣿⣿⠋⠀⠀⠀⢸⣿⣇⢹⣿⣷⣰⣿⣿⠃⠀⢠⣿⣿⢃⣀⣤⣤⣾⣿⡟⠀⠀⠀⢻⣿⣆⠀⠀
⠀⠀⠀⣿⣿⡇⠀⠀⢀⣴⣿⣿⡟⠀⣿⣿⣿⣿⠃⠀⠀⣾⣿⣿⡿⠿⠛⢛⣿⡟⠀⠀⠀⠀⠀⠻⠿⠀⠀
⠀⠀⠀⠹⣿⣿⣶⣾⣿⣿⣿⠟⠁⠀⠸⢿⣿⠇⠀⠀⠀⠛⠛⠁⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⠙⠛⠛⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

        You fell into a hole.
          ''')
    return False
        
def stage_two():
    choice = get_choice("You come to a lake. There is an island in the middle. Do you want to 'swim' or 'wait'? ", ["swim", "wait"])
    if choice == "wait":
        return True
    print('''    
          _.---._     
            __...---' .---. `---'-.   `.
  ~ -~ -.-''__.--' _.'( | )`.  `.  `._ :
 -.~~ .'__-'_ .--'' ._`---'_.-.  `.   `-`.
  ~ ~_~-~-~_ ~ -._ -._``---. -.    `-._   `.
    ~- ~ ~ -_ -~ ~ -.._ _ _ _ ..-_ `.  `-._``--.._
     ~~-~ ~-_ _~ ~-~ ~ -~ _~~_-~ -._  `-.  -. `-._``--.._.--''. ~ -~_
         ~~ -~_-~ _~- _~~ _~-_~ ~-_~~ ~-.___    -._  `-.__   `. `. ~ -_~
       ~~~_   ~~ _~- ~~- -_~  ~- ~ - _~~- _~~ ~---...__ _    ._ .` `. ~-_~
                ~ ~- _~~- _-_~ ~-_ ~-~ ~_-~ _~- ~_~-_~  ~--.....--~ -~_ ~
                     ~ ~ - ~  ~ ~~ - ~~-  ~~- ~-  ~ -~ ~ ~ -~~-  ~- ~-~
                     
           You were attacked by a crocodile.          
          ''')
    return False

def stage_three():
    choice = get_choice("You arrive at the island. There is a house with 3 doors: red, blue, and yellow.\nWhich one do you choose? ",
        ["red", "blue", "yellow"])
    if choice == "yellow":
        print('''
               ______________
|\ ___________ /|
| |  /|,| |   | |
| | |,x,| |   | |
| | |,x,' |   | |
| | |,x   ,   | |
| | |/    |%==| |
| |    /] ,   | |
| |   [/ ()   | |
| |       |   | |
| |       |   | |
| |       |   | |
| |      ,'   | |
| |   ,'      | |
|_|,'_________|_| 

    You open the yellow door and find a dazzling treasure chest filled with gold and jewels. Congratulations, you found the treasure!
              ''')
        return True
    elif choice == "red":
        print('''
               ______________
|\ ___________ /|
| |  /|,| |   | |
| | |,x,| |   | |
| | |,x,' |   | |
| | |,x   ,   | |
| | |/    |%==| |
| |    /] ,   | |
| |   [/ ()   | |
| |       |   | |
| |       |   | |
| |       |   | |
| |      ,'   | |
| |   ,'      | |
|_|,'_________|_| 

    As you open the red door, a burst of flames engulfs you. It's a trap! You were burned alive. 
    
    Game Over.
              ''')
    elif choice == "blue":
        print('''
               ______________
|\ ___________ /|
| |  /|,| |   | |
| | |,x,| |   | |
| | |,x,' |   | |
| | |,x   ,   | |
| | |/    |%==| |
| |    /] ,   | |
| |   [/ ()   | |
| |       |   | |
| |       |   | |
| |       |   | |
| |      ,'   | |
| |   ,'      | |
|_|,'_________|_| 

    You step through the blue door and find yourself surrounded by growling beasts. They don't seem friendly. You were devoured. 
    
    Game Over.
              ''')
    return False

def main():
    
    if not stage_one():
        return
    
    if not stage_two():
        return
    
    stage_three()
    
if __name__ == "__main__":
    main()