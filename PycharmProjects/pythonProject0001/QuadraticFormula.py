print("Hello, Welcome to the Quadratic Formula Calculator... ")
print("This is the format of a Quadratic equation. ax^2+bx+c=0")
a = int(input("What is the Value of a? "))
b = int(input("What is the Value of b? "))
c = int(input("What is the Value of c? "))

value1 = (-b+((b**2)-4*(a*c))**0.5)/(2*a)

value2 = (-b-((b**2)-4*(a*c))**0.5)/(2*a)

print("One answer is: " + str(value1))
print("Another answer is: " + str(value2))