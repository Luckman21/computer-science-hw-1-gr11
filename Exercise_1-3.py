'''
Created on Mar 27, 2017

@author: Luqmaan
'''
'''
item = raw_input ("What did you buy today? ")

price = input ("How much was it")

dis = price * 0.1

cost = price + dis

print "Here is the total cost"

print cost


num = input ("Convert inches to centimeters")
print "The number below is the number of inches you have inputed which has been converted into centimeters"
print num * 2.54


a = input ("Enter value for A (make sure if number is a whole number add #.0)")
b = input ("Enter value for B (make sure if number is a whole number add #.0)")
c = input ("Enter value for C (make sure if number is a whole number add #.0)")
d = input ("Enter value for D (make sure if number is a whole number add #.0)")

print "Here is your result"
print a + b * c / d

'''
'''
hour1 = input ("What hour did you leave to get to the destination? (Please enter time in military time) ")
min1 = input ("What minute did you leave to get to the destination? (Please enter time in military time) ")

hour2 = input ("What hour did you arrive at the destination? ")
min2 = input ("What minute did you arrive at the destination? ")

hours = hour2 - hour1
mins = min2 - min1

dis = input ("How far did you travel in kilometers?")

print "Here is how long the trip took"
print
print "Hours:"
print hours
print
print "Minutes: "
print mins
print
print "Here is the average speed of the car in minutes:"

tothours = hours * 60.0

totmins = tothours + mins

speed = dis / totmins

print speed
print
print "Here is the average speed of the car in hours:"
print speed*60.0

'''
'''
a = input ("Enter your first number: ")
b = input ("Enter your second number: ")
c = input ("Enter your third number: ")
d = input ("Enter your fourth number: ")

print a, b, c, d 
'''
'''
a = raw_input ("Name character 1 ")
b = raw_input ("Name character 2 ")
c = raw_input ("Name character 3 ")
d = raw_input ("Name character 4 ")
e = raw_input ("Name character 5 ")

print e, d, c, b, a

'''
'''
name1 = raw_input ("Please enter name 1 ")
name2= raw_input ("Please enter name 2 ")

from random import randint

num = (randint(0.0,100.0))

print "Here is a cool number"
print num
'''
'''
first = raw_input ("Please enter your first name ")
last = raw_input ("Please enter last name ")
print last, first
'''


name = input_names.split("Please enter both your first and last name: ")\

print

'''

a = raw_input ("Please enter a noun")
e = raw_input ("Please enter a verb")
i = raw_input ("Please enter an adjective")
b = raw_input ("Please enter a noun")
f = raw_input ("Please enter a verb")
j = raw_input ("Please enter an adjective")
c = raw_input ("Please enter a noun")
g = raw_input ("Please enter a verb")
k = raw_input ("Please enter an adjective")
d = raw_input ("Please enter a noun")
h = raw_input ("Please enter a verb")
l = raw_input ("Please enter an adjective")

print a, h, k, b, f, j, c, e, l, d, g, i
'''



