# main.py
print("=== Create Account (Python Simulation) ===")

while True:
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    # Username validation
    if username == "":
        print("❌ Username cannot be empty.")
    elif username.isdigit():
        print("❌ Username cannot be only numbers.")
    elif username.isalpha():
        print("❌ Username must contain at least one number.")
    elif len(username) < 7:
        needed = 7 - len(username)
        print(f"❌ Your username is too short. Add {needed} more character(s) to proceed.")
    else:
        print("✅ Username accepted.")

    # Password validation
    if len(password) < 10:
        needed = 10 - len(password)
        print(f"❌ Your password is too short. Add {needed} more character(s) to proceed.")
    elif len(password) > 20:
        print("❌ Your password is too long. Maximum is 20 characters.")
    else:
        if any(ch.isdigit() for ch in password) and any(ch.isalpha() for ch in password):
            print("✅ Password accepted.")
            print(f"🎉 Account created successfully for {username}!")
            break
        elif password.isdigit():
            print("❌ Password must contain letters.")
        elif password.isalpha():
            print("❌ Password must contain numbers.")
        else:
            print("❌ Password must contain both letters and numbers.")

    print("Try again.\n")

print("\nFinalizing account setup...")
for step in range(1, 4):
    print(f"Step {step}: Processing...")

print("✅ Setup complete. Welcome!")
