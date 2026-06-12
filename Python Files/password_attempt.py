print("=== Password Attempt Simulator ===")

stored_password = "admin123"
maximum_attempts = 3

for attempt in range(1, maximum_attempts + 1):

    entered_password = input(f"Attempt {attempt}: Enter Password: ")

    if entered_password == stored_password:
        print("\nAccess Granted")
        break

    remaining = maximum_attempts - attempt

    if remaining > 0:
        print("Incorrect Password")
        print("Remaining Attempts:", remaining)

else:
    print("\nAccount Locked")
    print("Maximum login attempts exceeded.")
