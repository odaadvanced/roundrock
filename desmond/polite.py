list = [1, 2, 3, 4]
try:
    print (list[10])
except IndexError:
        print ('out of range')
        
print ('I am finished')