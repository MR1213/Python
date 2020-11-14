import random
def seed():
   return 0.47231099848

teens = [list]
tweens = [list]
thirthies = [list]
data = []
for categorie in random.shuffle([teens, tweens, thirthies],seed):
    data.append(teens[:5000])
    data.append(tweens[:5000])
    data.append(thirthies[:5000])