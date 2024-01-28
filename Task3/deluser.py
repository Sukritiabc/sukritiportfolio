def delete_user(username):
    try:
        with open("passwd.txt", "r") as file:
            lines = file.readlines()

        with open("passwd.txt", "w") as file:
            user_found = False
            for line in lines:
                existing_username = line.split(":")[0].strip().lower()
                if existing_username != username:
                    file.write(line)
                else:
                    user_found = True

            if user_found:
                print("User Deleted.")
            else:
                print("User not found. No change made.")
    except FileNotFoundError:
        print("File not found. No change made.")

if __name__ == "__main__":
    delete_username = input("Enter username: ").strip().lower()
    delete_user(delete_username)
