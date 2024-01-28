import getpass
def add_user(username, real_name, password):
    try: #in case of error
        with open("passwd.txt", "a") as file: #filr handling
            file.write(f"{username}:{real_name}:{password}\n") #format of text
            print("User Created.")
    except Exception as e:
        print(f"Error: {e}") 

if __name__ == "__main__":
    new_username = input("Enter new username: ").strip().lower() #removing whitespaces and lower casing
    new_real_name = input("Enter real name: ").strip()
    new_password = getpass.getpass("Enter password: ").strip()

    try:
        with open("passwd.txt", "r") as file:
            for line in file:
                existing_username = line.split(":")[0].strip().lower() #stripping whitespace from input("Enter new username: ") after username
                if existing_username == new_username: #no two username can be the same
                    print("Cannot add. Most likely username already exists.")
                    exit()
                existing_password = line.split(":")[0].strip().lower()
                if existing_password == new_password: #no two passwords can be the same
                    print("Cannot add. Most likely password already exists.")
                    exit()


        add_user(new_username, new_real_name, new_password)
    except FileNotFoundError: #if no error then continues as normal
        add_user(new_username, new_real_name, new_password)
