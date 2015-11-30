import random



def monty_hall():
    choices = ["A","B","C"]
    doors = shuffle_doors()
    print("\nWelcome to the monty hall show or whatever!")
    print("\nIn this show there are three doors")
    print_doors()
    print("Behind two are goats, and behind the third is a")
    print("BRAND NEW CAR o man\n")
    
    print("So please choose between door a b and c")
    
    choice = input("A B or C? ")
    
    badchoice = True
    while(badchoice):
        choice = choice.upper()
        if(not(choice in choices)):
            choice = input("I said A B OR C. ")
        else:
            badchoice = False
            
    choices.remove(choice)
    
    print("We will now reveal a goat behind one of the other doors.")
    input()
    choices.remove(open_door(choices,doors))
    
    print("\nWould you like to switch to door {0}?".format(choices[0]))
    answer = input("y/n? ")
    
    if(answer.lower() == "y"):
        choice = choices[0]
        print("You have switched to door {0} \n".format(choice))
    
    print("And behind door {0} is...".format(choice))
    input()
    
    if(doors[choice] == "car"):
        print_car()
        
    else:
        print_goat()
        print("a goat. congrats.")
        
    print("That's the end of our show today!")
   


def shuffle_doors():

    prizes = ["goat","goat","car"]
    
    random.shuffle(prizes)
    doors = {"A":"","B":"","C":""}
    i = 0
    for door in doors:
        doors[door] = prizes[i]
        i += 1
    return doors
def open_door(choices,doors):
    for choice in choices:
        if(doors[choice] == "goat"):
            print_goat()
            print("There was a goat behind door " + choice)
            return choice


def print_car():
    print("""

                   .--------.
              ____/_____|___ \___
             O    _   - |   _   ,*
              '--(_)-------(_)--' 
    
    a car, you won it. woo
    """)

def print_goat():
    print("""
                (_(
                /_/'_____/)
                \"  |      |
                   |\"\"\"\"\"\"|
        
    """)
    
    
def print_doors():
    print("""
         _    _    _
        |a|  |b|  |c|                            
        | |  | |  | |
    """)
    
monty_hall()