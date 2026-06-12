print("=== Number Analysis Tool ===")

n = int(input("Enter a positive number: "))

total_sum = 0
even_count = 0
odd_count = 0

for number in range(1, n + 1):

    total_sum += number

    if number % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("\nAnalysis Result")
print("-" * 25)
print("Sum of numbers from 1 to", n, "=", total_sum)
print("Count of Even Numbers =", even_count)
print("Count of Odd Numbers =", odd_count)
