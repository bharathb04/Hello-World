# Hello World program in Python
#!/usr/bin/python
import sys
##print "Counted", len(data), "lines."
#learning python 
print "Hello, Python!"
name = sys.stdin.readline()
num1 = int(sys.stdin.readline())
num2 = int(sys.stdin.readline())
num3 = int(sys.stdin.readline())
num4 = int(sys.stdin.readline())

print "Your name is " + name

res2 = int(num4 % 2)

if res2 == 0:
   print "Num4 is Even"
else:
   print "Num4 is Odd"
