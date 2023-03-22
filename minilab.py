import re
f = open('Login-Authenticator/emails_passwords.txt','r')
x = f.read()
store = []

def userinput():
    f = open('emails_passwords.txt', 'a')
    email = input("Please input your email: ")
    store.append(email)
    pattern = "^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).*$"
    password = input("Please enter a password: ")
    verification = re.findall(pattern, password)
    if verification:
        print("Valid password")
        line_addition = email + "" + password
        f.write(line_addition + "\n")
        f.close()
    else:
        print("Password not valid")
        store.pop(-1)


def login_authenticator():
    username = input("Please enter your email.\n")
    password = input("Please enter your password.\n")
    with open('Login-Authenticator/emails_passwords.txt', 'r') as f:
        contents = f.read()
        lines = contents.split("\n")
        for line in lines:
            line_parts = line.split(" ")
            if username == line_parts[0] and password == line_parts[1]:
                validation = True
                break
        else:
            validation = False
    
    if validation == True:
        print("Welcome to Omar's program!!!")
    else:
        return login_authenticator()

def  login_type():
    print("Welcome to the login portal.", "\n", "Would you like to create a new login?\n")
    type_checker = input("Please type Y for new login or N for existing.:\n")
    if type_checker == "Y":
        return userinput()
    else:
        return login_authenticator()

login_type()

    


