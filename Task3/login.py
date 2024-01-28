import getpass
import subprocess

def login(username, password):
    try:
        with open("passwd.txt", "r") as file:
            for line in file:
                parts = line.split(":")
                existing_username = parts[0].strip().lower()
                existing_password = parts[2].strip()

                if existing_username == username and existing_password == password:
                    return True

        return False
    except FileNotFoundError:
        print("File not found. Access denied.")
        return False

def add_user():
    subprocess.run(["python", "Task3/adduser.py"])

def delete_user():
    subprocess.run(["python", "Task3/deluser.py"])

def change_password():
    subprocess.run(["python", "Task3/passwd.py"])

if __name__ == "__main__":
    login_username = input("User: ").strip().lower()
    login_password = getpass.getpass("Password: ")

    if login(login_username, login_password):
        print("Access granted.")

        # Options after successful login
        print("Choose an option:")
        print("1. Add User")
        print("2. Delete User")
        print("3. Change Password")

        choice = input("Enter the option number: ")

        if choice == "1":
            add_user()
        elif choice == "2":
            delete_user()
        elif choice == "3":
            change_password()
        else:
            print("Invalid option.")
    else:
        print("Access denied.")
