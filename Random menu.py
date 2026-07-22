import random

breakfast = [
    "Toast", "Cereal", "Pancakes", "Waffles", "Bagel",
    "Croissant", "Eggs", "Porridge", "Yogurt", "Fruit"
]

lunch = [
    "Sandwich", "Burger", "Pizza", "Pasta", "Salad",
    "Wrap", "Chicken, RIce and Curry", " Corn Soup", "Fish and Chips", " Paneer Noodles"
]

snacks = [
    "Chips", " Chocolate chip Cookies", "Popcorn", "Chocolate", "Fruit salad",
    "  Blueberry Muffin", "Crackers", "Ice Cream", "Cupcake", "Pretzels"
]

dinner = [
    "Pizza", "Pasta", "Roast Chicken", "Curry and rice", " Steamed Fish",
    "Burgers", "Tacos", " Vegetable Lasagna", "Sushi", "Mac and Cheese"
]

menu = {
    "Breakfast": random.choice(breakfast),
    "Lunch": random.choice(lunch),
    "Snacks": random.choice(snacks),
    "Dinner": random.choice(dinner)
}


menu = f"""
+--------------+----------------+
|  Today's Menu                |
+--------------+----------------+
| Breakfast    | {random.choice(breakfast)}
+--------------+----------------+
| Lunch        | {random.choice(lunch)}
+--------------+----------------+
| Snacks       | {random.choice(snacks)}
+--------------+----------------+
| Dinner       | {random.choice(dinner)}
+--------------+----------------+
"""

print(menu)
