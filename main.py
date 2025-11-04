
import pygame
pygame.init()
import random
import itmes_drops


#monster_decision
castle_key = False
#goblin
gold_coin = 0
sword = False
health_potion = 0
#dragon
dragon_scales = 0
gold_bars = 0
fire_gem = False
#zombie
rotten_flesh = 0
bones = 0
invisible_ring = False

attacking = False
in_castle = False
outside_caslte = True
#path tracking
path_movment = 0

health = 100
#the dice roller

print("This is a dice roller game. You roll dice to see what you do while trying to go up the path into the castle to get to the stash of gold!")
print("You need to go up the path 20 times to get in the castle and 10 times in the castle before you win.")
print("Word on the street says that there is three dragons gaurding the gold from inside the castle.")
#-----loop
running = True
while running:
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #action decision
    current_roll = random.randint(1, 6)
    current_monster = random.randint(1,2)
     
    if current_monster == 1 or not sword:
        monster = "Goblin"
    
    if current_monster == 2:
        monster = "Zombie"
        
    
    #checking inventory
    def not_in_castle():

        ready = input("Are you ready to roll the dice?")
        if current_roll == 1:
            current_action = print("You decide not to move up the path and take a second to look at your inventory")
            
            print("Would you like to look at how many health potions, gold coin or gold bars, or your current health?")
            print("Make sure to specify what you would like to look at, saying current health would print your current health.")
            print("If you are done looking type 'go' to exit and continue")
            while True:
                active_inventory_look = input()
                    
                if active_inventory_look == "health potions":
                   print("You currently have " + str(health_potions) + " Health Potions.")
                    
                elif active_inventory_look == "gold coins":
                    print("You currently have " + str(gold_coins) + " Gold Coins.")
                    
                elif active_inventory_look == "gold bars":
                    print("You currently have " + str(gold_bars) + " Gold Bars")
                        
                elif active_inventory_look == "current health":
                    print("Your current health is " + str(health))
                        
                elif active_inventory_look == "go":
                  break
                        
                else:
                    print("Make sure to type it correctly and lower case.")    
        
        #move up path without monsters
        if current_roll == 2 or current_roll == 3 or current_roll == 4:
            current_action = print("You move up the path without any monsters getting in your way")
            path_movement += 1
        
        #move up path with monsters
        if current_roll == 5 or current_roll == 6:
            attacking = True
            
            if monster == "Goblin" and not sword:
                print("You have fought the goblin and won but not without losing some health point.")
                health -= 5
            elif monster == "Goblin" and sword:
                print("You have defeted the goblin and have not gotten hit.")
            
            if monster == "Zombie":
                print("You have defeted the zombie but have taken a little damage.")
                health -= 5
                
            if health == 0:
                print("You have died.")
                running = False
                    
            drop = items_drops.get_monster_drop(monster)
            print(f"The {monster} dropped: {drop}")
                
            if drop == "Sword":
                sword = True
            
            elif drop == "Health Potion":
                health_potion += 1
                
            elif drop == "Gold Coins":
                gold_coins += 3
                
            elif drop == "Gold Bar":
                gold_bar += 1
            
            elif drop == "Invisable Ring":
                invisable_ring = True
    
            path_movement += 1
    going_game = not_in_caslte()
    print(going_game)
