car1 = 'true'
car2 = 'false'
car3 = 'true'
light1 = 'Left: green Forward: green'
light2 = 'Left: green Right: green'
light3 = 'Right: green Forward: green'

highway1 = 'main'
#highway = 'secondary'

existcar1 = str(input("Car #1\n___________________________\nYes or No? \n"))
existcar2 = str(input("Car #2\n___________________________\nYes or No? \n"))
existcar3 = str(input("Car #3\n___________________________\nYes or No? \n"))

if existcar1 == 'true' and existcar3 == 'true':
    highway1 = 'main'
    light1 = 'Left: red Forward: green'
    light2 = 'Left: red Right: red'
    light3 = 'Right: green Forward: green'
if existcar2 == 'true' and existcar3 == 'true':
    highway1 = 'secondary'
    light1 = 'Left: red Forward: red'
    light2 = 'Left: red Right: green'
    light3 = 'Right: green Forward: green'
if existcar2 == 'true' and existcar3 == 'true':
    highway1 = 'main'
    light1 = 'Left: green Forward: green'
    light2 = 'Left: red Right: green'
    light3 = 'Right: green Forward: red'

print("Light 1: \n" + str(light1) + "\nLight 2: \n" + str(light2) + "\nLight 3: \n" + str(light3))