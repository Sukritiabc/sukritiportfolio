import getpass
def add_user(username, real_name, password):
    try:
        with open("passwd.txt", "a") as file:
            file.write(f"{username}:{real_name}:{password}\n")
            print("User Created.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    new_username = input("Enter new username: ").strip().lower()
    new_real_name = input("Enter real name: ").strip()
    new_password = input("Enter password: ").strip()

    try:
        with open("passwd.txt", "r") as file:
            for line in file:
                existing_username = line.split(":")[0].strip().lower()
                if existing_username == new_username:
                    print("Cannot add. Most likely username already exists.")
                    exit()
                existing_password = line.split(":")[0].strip().lower()
                if existing_password == new_password:
                    print("Cannot add. Most likely password already exists.")
                    exit()


        add_user(new_username, new_real_name, new_password)
    except FileNotFoundError:
        add_user(new_username, new_real_name, new_password)
