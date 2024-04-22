from cryptography.fernet import Fernet

"""def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
        
write_key()"""

def load_key():
    with open("password_manager/key.key", "rb") as file:
        key = file.read()
        return key

key = load_key()
fer = Fernet(key)

def add():
    name = input("Enter account: ")
    pwd = input("Enter a password: ")
    with open('password_manager/passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

def view():
    with open("password_manager/passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("Account:", user, "| Password:", fer.decrypt(passw.encode()).decode())

def manager():            
    while True:
        user = input("What would you like to do: add or view your password? Press q to quit: ")
        if user == 'q':
            print("Exiting Password Manager")
            break
        
        if user.lower() == 'add':
            add()
        elif user.lower() == 'view':
            view()
        else:
            print("Invalid input")
            continue

if __name__ == "__main__":
    manager()