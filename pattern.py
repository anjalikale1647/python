print("\n*************** INVOICE STAR PATTERN ****************\n")

rows = 8
cols = 40

for i in range(rows):
    for j in range(cols):
        if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

print("\n*************** INVOICE NUMBER PATTERN ****************\n")

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

print("\n*************** RECEIPT NUMBER PATTERN ****************\n")

rows = 12
cols = 35

for i in range(rows):
    for j in range(cols):
        if i == 0 or i == rows - 1:
            print(j % 10, end="")
        elif j == 0 or j == cols - 1:
            print(i % 10, end="")
        else:
            print(" ", end="")
    print()

print("\n*************** RECEIPT STAR PATTERN ****************\n")

rows = 12
cols = 35

for i in range(rows):
    for j in range(cols):
        if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()