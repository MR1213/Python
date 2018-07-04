def my_range(start, end, step):
    while start <= end:
        yield start
        start += step



def toInches(cm):
    return cm/2.54

inches=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40]


def toCentimeters(i):
    return i*2.54


for cm in my_range(0,100000,1):
    i=toInches(cm)
    cm = toCentimeters(i)
    print(str(cm) + ":" + " -> " + str(i))