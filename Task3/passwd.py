def change_password(username, current_password, new_password):
    try:
        with open("passwd.txt", "r") as file:
            lines = file.readlines()

        with open("passwd.txt", "w") as file:
            user_found = False
            for i, line in enumerate(lines):
                parts = line.split(":")
                existing_username = parts[0].strip().lower()
                existing_password = parts[2].strip()
                
                if existing_username == username:
                    user_found = True
                    if new_password == existing_password:
                            print("same password given. give different password")
                            exit()
                    elif existing_password == current_password:
                        new_password_confirm = input("Confirm: ").strip()
                        
                        if new_password == new_password_confirm:
                            parts[2] = new_password
                            file.write(":".join(parts))
                            print("Password changed.")
                       
                        else:
                            print("Passwords do not match. No change made.")
                    
                    else:
                        print("Invalid current password. No change made.")
                else:
                    file.write(line)

            if not user_found:
                print("User not found. No change made.")
    except FileNotFoundError:
        print("File not found. No change made.")

if __name__ == "__main__":
    change_username = input("User: ").strip().lower()
    current_password = input("Current Password: ").strip()
    new_password = input("New Password: ").strip()

    change_password(change_username, current_password, new_password)
