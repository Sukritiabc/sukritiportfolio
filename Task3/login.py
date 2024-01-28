import getpass #enryption using getpass
import subprocess #to use external file like using command line

def login(username, password):
    try:
        with open("passwd.txt", "r") as file:
            for line in file:
                parts = line.split(":")
                existing_username = parts[0].strip().lower()
                existing_password = parts[2].strip()
                #checking username and password
                if existing_username == username and existing_password == password:
                    return True

        return False
    except FileNotFoundError: #error handling when file is not found
        print("File not found. Access denied.")
        return False
#linking the other files to the main file
def add_user():
    subprocess.run(["python", "Task3/adduser.py"])

def delete_user():
    subprocess.run(["python", "Task3/deluser.py"])

def change_password():
    subprocess.run(["python", "Task3/passwd.py"])

if __name__ == "__main__":
    #asking for username and password
    login_username = input("User: ").strip().lower() 
    login_password = getpass.getpass("Password: ")

    if login(login_username, login_password):
        print("Access granted.")

        # Options after successful login
        print("Choose an option:")
        print("1. Add User")
        print("2. Delete User")
        print("3. Change Password")
        print("4 exit")

        choice = input("Enter the option number: ") #choose an option

        if choice == "1":
            add_user() #adds another username
        elif choice == "2":
            delete_user() #deleting username
        elif choice == "3":
            change_password() #changing password of any user
        elif choice == "4":
            exit()
        else:
            print("Invalid option.")
    else:
        print("Access denied.")
