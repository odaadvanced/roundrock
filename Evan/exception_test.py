list = [1,3,5,7,9,11,13,15,17,19,21]
try:
    print(list[13])
except IndexError:
    print("out of range")
print ("I am finished")
