import random

prefixes = [
    "Mega", "Turbo", "Captain", "Professor", "Fluffy",
    "Dancing", "Flying", "Cosmic", "Epic", "Wobbly",
    "Rainbow", "Banana", "Pickle", "Dragon", "Ninja",
    "Zombie", "Pirate", "Mystery", "Golden", "Ancient",
    "Cherry", "Blush", "Velvet", "Pearl", "Rosie",
    "Sugar", "Ribbon", "Dreamy", "Sparkly", "Honey",
    "Moonlit", "Bubblegum", "Princess", "Bunny", "Cupid",
    "Invisible", "Exploding", "Chaotic", "Legendary", "Funky"
]

suffixes = [
    "Mart", "Shop", "Store", "Factory", "Warehouse",
    "Palace", "Dungeon", "Laboratory", "Headquarters",
    "Kingdom", "Castle", "Arena", "Circus", "Bazaar",
    "Dimension", "Galaxy", "Hideout", "Boutique",
    "Garden", "Manor", "Cottage", "Atelier",
    "Dreamland", "Corner", "Express", "Station",
    "Co.", "Unlimited", "and Sons", "Emporium",
    "Paradise", "Treasures", "Workshop", "Universe"
]


word = input("Enter a word: ")

shop_name = f"{random.choice(prefixes)} {word.capitalize()} {random.choice(suffixes)}"

print("Your custom shop name:")
print(shop_name)
