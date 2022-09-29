import random
x = 0
print("total, condition, repeat number")
while x<=10:
    total =  random.randint(-10, 10)
    if total >= 5 and total <= 9:
        print((total), ('not bad,'), x)
        x += 1
    if total >= 9 or total <= 5:
        print((total), ('VERY VERY BAD!!!,'), x)
        x += 1