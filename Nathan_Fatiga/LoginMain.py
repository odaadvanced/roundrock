import random

lgns = ((("Nathan Fatiga"), ("NaThAn11")), (("test"), ("12345")))

mailNaThAn11 = ("No New Mail")

def Login():
    username = input("Username: ")
    password = input("Password: ")
    if (username, password) in lgns:
        print("welcome back", username)
        create_security_password()
    else:
        print("error")
        Login()

def create_security_password():
    global securitypswd1
    global securitypswd2
    global securitypswd3
    securitypswd1 = input("What is your favorite color?\n")
    securitypswd2 = input("What street do you live on?\n")
    securitypswd3 = input("What is your dog's name?\n")
    Login2()

def Login2():
    global un
    global pw
    un = input("Username: ")
    pw = input("Password: ")
    if (un, pw) in lgns:
        qstn = random.randint(1, 3)
        if qstn == 1:
            sp1 = input("What street do you live on? ")
            if sp1 == securitypswd2:
                print("SUCCESS")
                Menu()
            else:
                print("ERROR")
        elif qstn == 2:
            sp2 = input("What is the name of your dog? ")
            if sp2 == securitypswd3:
                print("SUCCESS")
                Menu()
            else:
                print("ERROR")
        elif qstn == 3:
            sp3 = input("What is your favorite color? ")
            if sp3 == securitypswd1:
                print("SUCESS")
                Menu()
            else:
                print("ERROR")
        else:
            print("WHAT?")
    else:
        print("ERROR")

def Menu():
    print("Mail, Word Game, Settings, Exit")
    cs = input(": ")
    if cs == "Exit":
        restart()
    elif cs == "Mail":
        Mail()
    elif cs == "Word Game":
        Word_Game()
    elif cs == "Settings":
        Settings()
    else:
        print("Error")
        Menu()

def Mail():
    getmail = ("mail"(pw))
    print(getmail)
    
def Settings():
    usern = un
    dispw = len(pw)
    print("Username:", un)
    print("Password:", "********") 

Login()