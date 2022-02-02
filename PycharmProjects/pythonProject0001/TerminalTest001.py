import sys
import os
args = sys.argv

os.mkdir(args[0])

MyFile = open('C:\\Users\\maxsu\\OneDrive\\Desktop\\Python tester\\PythonTerminalTest1.txt', 'w')
write = MyFile.write("Billy is " + str(args[1]) + " years old" + "\n")
MyFile.close()