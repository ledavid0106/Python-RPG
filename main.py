# As a developer, I want to make at least five commits on GitHub with descriptive messages.  
# As a user, I want an engaging story to be told using print() statements.  
# As a user, I want Hercules (and each enemy), to have health, attack power, and a List of attack names saved in a Dictionary. 
# As a user, I want the ability to select Hercules’ attack using a menu prompt. 
# As a user, I want the foe’s attack to be chosen at random. 
# As a user, I want the results of each attack to be logged in the terminal.  
# As a developer, I want to use an Attack() function that will terminate when Hercules or an enemy’s health reaches zero.  
# As a developer, I want my RunGame() function to call my other functions in a logical order that will determine game flow. 
# As a developer, I want all of my functions to have a Single Responsibility. Remember, each function should do just one thing!  
herk = {"health": 100, "attack_power": 25}
print(herk)


def starting():
    print("Welcome to the world of the Greek Gods! A world full of wonders and mysteries but also leeks danger. ")
def herc():
    print("Here we are witnessing our Hero Hercules facing one of his many trials to defeat his enemy but he needs your help! ")
    print(f"Let's take a look at how our Hero is doing. Hercules currently has Health: {herk['health']} and Attack Power: {herk['attack_power']}")
herc()