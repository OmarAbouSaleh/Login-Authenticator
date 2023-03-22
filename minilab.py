import re

f = open('emails_passwords.txt','r')
store = []

def userinput():
    email = input("Please input you email. ")
    store.append(email)


userinput()

def validate_password():
    pattern = "^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).*$"
    password = input("Please enter a password. ")
    verfication = re.findall(pattern, password)
    if (verfication):
        print("Valid password")
        store.append(password)
    else:
        print("Password not valid")
        store.pop(-1)

validate_password()