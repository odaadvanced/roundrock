grade = float (input("Enter a Grade:"))

if grade == 100:
    print("You got a PERFECT score!")
elif grade >= 101:
    print("You got extra credit, Hooray!")
elif grade >= 151:
    print("I know that you are joking with the grade number")
elif grade >= 96:
    print("You got an A+!")
elif grade >= 93:
    print("You got an A!")
elif grade >= 90:
    print("You got an A-!")
elif grade >= 86:
    print("You got a B+!")
elif grade >= 83:
    print("You got a B!")
elif grade >= 80:
    print("You got a B-!")
elif grade >= 76:
    print("You got a C+")
elif grade >= 73:
    print("You got a C")
elif grade >= 70:
    print("You got a C-")
else:
    print("You failed the class.")