def login_system():
    correct_username = "admin"
    correct_password = "1234"
    
    attempts = 0
    max_attempts = 3

    while attempts < max_attempts:
        try:
            username = input("Enter username: ").strip()
            password = input("Enter password: ").strip()

            if username == correct_username and password == correct_password:
                print("\nLogin Successful")
                return
            else:
                attempts += 1
                print(f"\nInvalid credentials! Attempts left: {max_attempts - attempts}\n")

        except Exception as e:
            print("Error occurred:", e)

    print("\nAccount Blocked (Too many failed attempts)")

login_system()
