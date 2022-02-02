print("Hello, Welcome to the Quadratic Formula Calculator... ")
print("This is the format of a Quadratic equation. ax^2+bx+c=0")
a = int(input("What is the Value of a? "))
b = int(input("What is the Value of b? "))
c = int(input("What is the Value of c? "))

value1 = (-b+((b**2)-4*(a*c))**0.5)/(2*a)

value2 = (-b-((b**2)-4*(a*c))**0.5)/(2*a)

print("Value 1 is: " + str(value1))
print("Value 2 is: " + str(value2))