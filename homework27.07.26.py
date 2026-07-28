movies = ["The Rookie", "The Good Doctor", "Grey's Anatomy", "American Housewife", "Monsters Inc"]

for i in range(len(movies)):
    print(f"{i + 1}. {movies[i]}")


seating_plan = [
    ["Bavitha", "Sundy", "Amelia"],
    ["Ria", "Chloe", "Florence"],
    ["Olivia", "Millie", "Eva"]
]

print("Seating Plan:")
print()

for row in seating_plan:
    for seat in row:
        print(seat, end="\t")
    print()
