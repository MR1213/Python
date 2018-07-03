strs = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'      #use a string like this, instead of ord()
def shifttext(inp, shift):
    #inp = raw_input('Input text here: ')
    data = []
    for i in inp:                     #iterate over the text not some list
        if i.strip() and i in strs:                 # if the char is not a space ""  
            data.append(strs[(strs.index(i) + shift) % 26])
        else:
            data.append(i)           #if space the simply append it to data
    output = ''.join(data)
    return output

print(shifttext("Liam today I wrote a python code to make secret codes", 10))

height=1.5
age=14
if height > 1 and age > 12:
    print ('yes')
else: print('NO!')



word=""
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
