def get_input(*args):
    print(args)
    
def cpu_choice(cpu):
    print(random.cpu_choice("R,S,P"))
    cpu_choice("R,S,P")
    cpu_choice = ("R", "S", "P")

    User_choice("R")
user_choice = input("Make a choice. R stands for Rock, stands for Scissors, P stands for Paper.")
if user_choice == "R":
    
    print("You playaed R")
    import time
    time.sleep(0)

    print("cpu choice is")

    import random

    cpu_choice = ["R", "S", "P"]
    print(random.choice(cpu_choice))

    if cpu_choice == "R":
        print("Tie. Play  again.")
        
        def get_input(*args):
            print(args)
            
            player_choice("S")
            
            player_choice = input("Make a choice. R stands for Rock, stands for Scissors, P stands for Paper.")
            
            if player_choice == "S":
                print("You playaed S")
            
                import time
                time.sleep(0)
                print("cpu choice is")
                import random
                cpu_choice = ["R", "S", "P"]
                print(random.choice(cpu_choice))
                if cpu_choice == "P":
                    print("player won")

