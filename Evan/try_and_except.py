def divide(num1, num2):
    try:
        print(num1 / num2)
    except TypeError:
        print("Both arguements must be numbers")
    except ZeroDivisionError:
        print("num2 must not be 0")