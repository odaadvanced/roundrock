password = "NaThAn11"
username = "Nathan Fatiga"
u = input("insert username here: ")
if u == username:
    p = input("insert password here: ")
    if p == password:
        print("Welcome back", username)
    else:
        print("error")
else:
    print("error")