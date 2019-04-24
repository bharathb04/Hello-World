# Hello World program in Python
#!/usr/bin/python
import sys
##print "Counted", len(data), "lines."
#learning python 
print "Hello, Python!"
######

list_a = [7,8,14,2,3,14,1,18]

list_b = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

list_c = []

   
for element in list_b:

    if element < 5:
       list_c.append(element)    
       print(element)


print list_c
print "End Python"
