print("=== Multiplication Table Generator ===")

number = int(input("Enter a number: "))

print("\nMultiplication Table of", number)
print("-" * 30)

for multiplier in range(1, 11):
    result = number * multiplier
    print(f"{number} x {multiplier} = {result}")

print("\nTable generated successfully.")
