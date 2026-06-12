print("=== Username Generator ===")

first_name = input("Enter First Name: ").strip().lower()
last_name = input("Enter Last Name: ").strip().lower()
birth_year = input("Enter Birth Year: ")

year_last_two = birth_year[-2:]

print("\nGenerated Username Suggestions")
print("-" * 35)

username1 = first_name + last_name + birth_year
username2 = first_name[0] + "." + last_name + year_last_two
username3 = last_name + "_" + first_name
username4 = first_name + "_" + birth_year
username5 = first_name + last_name[0] + year_last_two

print("1.", username1)
print("2.", username2)
print("3.", username3)
print("4.", username4)
print("5.", username5)
