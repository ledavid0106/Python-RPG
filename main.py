# As a developer, I want to make at least five commits on GitHub with descriptive messages.  
# As a user, I want an engaging story to be told using print() statements.  
# As a user, I want Hercules (and each enemy), to have health, attack power, and a List of attack names saved in a Dictionary. 
# As a user, I want the ability to select Hercules’ attack using a menu prompt. 
# As a user, I want the foe’s attack to be chosen at random. 
# As a user, I want the results of each attack to be logged in the terminal.  
# As a developer, I want to use an Attack() function that will terminate when Hercules or an enemy’s health reaches zero.  
# As a developer, I want my RunGame() function to call my other functions in a logical order that will determine game flow. 
# As a developer, I want all of my functions to have a Single Responsibility. Remember, each function should do just one thing!  
hercules = {"health": 101, "attack_power": 25}
hydra = {"health": 300, "attack_power": 50}
her_moves = {"Hype": +25, "Slash": 50, "Take Aim": 80, "Thunderbolt": 100}
hyd_moves = {"Dust Storm": -0, "Crunch": 30, "Ancient Power": 40, "Hyper Beam": 100}
enemy = "Hydra"
import random
def intro():
    intros = input("Would you like a review on how attacks and power dynamics work? Y or N ")
    if intros == "Y":
        print("Each entity has a base amount of health and attack power. They will also have 4 different 'moves' that they can perform! Some will do damage while others can provide buffs. For the 'moves' that can do damage, the base attack power will be added to the number that follows the 'move' and will inflict # amount of damage to the opponent.")
        start()
    else:
        start()
def start():
    print("Let's get started!")   
def starting():
    print("Welcome to the world of the Greek Gods! A world full of wonders and mysteries but also leeks danger. ")
def herc():
    print("Here we are witnessing our Hero Hercules facing one of his many trials to defeat his enemy but he needs your help! ")
    print(f"Let's take a look at how our Hero is doing. ")
def hyd():
    print("Seems like the monster our Hero is fighting is the 9 Headed Lernaean Hydra!")
def her_status():
    print(f"Hercules currently has Health: {hercules['health']} and Attack Power: {hercules['attack_power']}")
def hyd_status():
    print(f"The {enemy} has Health: {hydra['health']} and Attack Power: {hydra['attack_power']}")    
def att_move(move):
    if move == "Slash":
        return 50
    if move == "Take Aim":
        return 80
    if move == "Thunderbolt":
        return 100
def menu(moves):
    move = input(f"What move would you like to use? {(moves)} ")
    if move == "Hype":
        att = hercules.get("attack_power")
        att += 25
        global hercules
        hercules["attack_power"] = att
        print(f"Hercules attack power has risen to {hercules.get('attack_power')}")
    else:
        hydra_health = hydra.get("health")
        herc_att = (hercules["attack_power"] + att_move(move))
        result = (hydra_health - herc_att)
        global hydra
        hydra["health"] = result
        print(f"Hercules has used {move}!")
        print(f"Hydra now has {hydra['health']} health remaining")
def enemy(moves):
    return random.choice(moves)
def log():
    
    print(f"Hercules has used {menu}! {enemy} now has ")
