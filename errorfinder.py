def fun(a,b):
    return a/b

def fun2(a,b):
    if(a%b != 0):
        raise ValueError('Cannot divide ' + str(a) + ' to ' + str(b) + ' evenly')
    return a/b
def fun3 (a,b):
    if a<0:
        raise ValueError('Cannot divide ' + str(a) + ' to ' + str(b) + ' evenly')
def fun4 (a,b):
    if (a<200 & a>100):
        raise ValueError('Cannot divide ' + str(a) + ' to ' + str(b) + ' evenly')
arr=[12,14,16,18,-50,38,59,191,34,-11,-23,68,35,0,173]
for a in arr:
    try:
        print(str(a) + ": " + str(fun2(100,a)))
    except:
        print("Error!!!: "+str(a))