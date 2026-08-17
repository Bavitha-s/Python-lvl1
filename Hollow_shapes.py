#hollow rectangle

rows = int(input("Enter the height: "))
cols = int(input("Enter the width: "))

print("\nHollow Rectangle:\n")

for row in range(rows):
    for col in range(cols):
        if row == 0 or row == rows - 1 or col == 0 or col == cols - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

    
    # suggest row number startign w 1
    
# hollow triangle

rows = int(input("Enter number of rows: "))

for row in range(1, rows + 1):
    for col in range(1, row + 1):
        if col == 1 or col == row or row == rows:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
