print("=== Pattern Printing Program ===")

print("\nPattern 1")
for row in range(1, 6):
    print("*" * row)

print("\nPattern 2")
for row in range(5, 0, -1):
    print("*" * row)

print("\nPattern 3")
for row in range(1, 6):

    for column in range(1, row + 1):
        print(column, end="")

    print()
