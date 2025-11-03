
import random


monster_drops = {
    "Goblin": {"Gold Coin": 50, "Sword": 30, "Health Potion": 20},
    "Dragon": {"Dragon Scale": 60, "Gold Bar": 30, "Fire Gem": 10},
    "Zombie": {"Rotten Flesh": 60, "Bone": 30, "Invisable Ring": 10},
    "Goul": {"Castle Door Key": 100}
}

# Simulating a drop with probabilities
def get_monster_drop(monster):
    if monster in monster_drops:
        items = list(monster_drops[monster].keys())
        probabilities = list(monster_drops[monster].values())
        return random.choices(items, probabilities, k=1)[0]
    else:
        return "No drops available for this monster."

"""
Example usage
monster = "Dragon"
drop = get_monster_drop(monster)
print(f"The {monster} dropped: {drop}")

"""
