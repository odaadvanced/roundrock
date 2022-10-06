list = [1,2,3,4,5,6,7,8,9,10]
try:
    print (list[10])
except IndexError:
    print ('out of range')
print ('I am Finished')