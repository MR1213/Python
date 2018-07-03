def wordanalyz(word):
    d=0
    v=0
    S=0
    u=0
    al=0
    co=0
    lc=0
    concenents="qwrtpsdfghjklmnbvcxz"
    vowels="eyuioa"
    symbols="~`!@#$%^&*()_-+={[}]:;|<,>.?/\"'\\"

    for ch in word:
        #check for digits
        if ch.isdigit():
            d = d + 1

        #check for letters
        if ch.isalpha():
            al = al + 1

        if ch.islower():
            lc = lc + 1
        if ch.isupper():
            u = u + 1

        #check for vowels
        if ch in vowels:
            v = v + 1
        if ch in symbols:
            S=S+1
        if ch in concenents:
            co = co + 1
    print("concenents:"+ str(co))
    print("digits: " + str(d))
    print("uppercase: "+ str(u))
    print("letters: " + str(al))
    print("vowles: " + str(v))
    print("lowercace: " + str(lc))
    print("symbols: " + str(S))
    print("length: " + str(len(word)))

words = ["Hi","Hello","my","my", "name", "is"," jeff",]

for word in words:
    print("******************************************************************************")
    wordanalyz(word)