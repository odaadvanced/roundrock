import random
for x in range(1, 11):
    random_number = random.randint(1, 13)
    print(random_number)
    if random_number >=5 and random_number <= 9 :
        print ("alright")
    if random_number >=1 and random_number <= 4 :
        print ("you gonna cry?")
    if random_number >=10 and random_number <= 12 :
        print ("nice")