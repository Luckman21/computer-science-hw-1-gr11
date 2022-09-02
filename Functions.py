'''
Created on Apr 9, 2018

@author: Luck
'''
''' Functions
def pnum(n):
    return n

def rnum(n):
    return n
    
def addThree(n):
    return n + 3

f1 = pnum(7)
f2 = rnum(2)

print f1
print f2

f3 = addThree(2)
print f3
f4 = addThree(1)
print f4
'''

'''recursion
This is when the function calls itself from within the function'''
'''
def hyp(a,b):
    'Returns the hypotenuse of a and b'
    c = (a**2 + b**2)**(0.5)
    return c

num1 = input(": ")
num2 = input(": ")
print hyp(num1,num2)
'''

def occ(a,b):
    'Counts the number of times b is found in a'
    count = 0
    
    if len(b) > len(a):
        pass
    else:
        for x in range (0,len(a)):
            time = 0
            if a[x] == b[0]:
                for y in range(0,len(b)):
                    if x+y > len(a):
                        break
                    elif b[y] == a[x+y]:
                        time+=1
            if time == len(b):
                count+=1
    return count

str1 = raw_input("Enter a string sequence: ")
str2 = raw_input("Enter a string sequence: ")

print "The number of times "+str1+" appears in "+str2+" is: "+str(occ(str1,str2))