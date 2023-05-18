num = float(input("what grade did you get???"))


if num >= 90 and num <= 100:
    print("YOU PASSED THE CLASS WITH AN A!!! INCREDIBLE!!!")
 
elif num > 100:
    print("invalid grade entered, a 0 has been recorded in the grade book")   

elif num >= 80:
    print("You passed the class with a B, Nice Job.")
    
elif num >= 70:
    print("you barely slid by with a c, OK i guess.")
    
if num < 70:
    print("you did trash, you failed loser")