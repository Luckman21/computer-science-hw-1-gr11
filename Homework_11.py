'''
Created on May 3, 2017

@author: Luqmaan
'''
'''
num = 0
while True:
    num+=1
    print num
'''
'''
while True:
    
    age = input ("What is my age?\n:")
    
    if age == 15:
        print "Cool."
        break
        
    else:
        print "Try again."

num = 0
while True:
    num = input ("Player 1, enter a number between 1 and 10: ")
    print "\n"*1000
    
    if num >= 1 and num <= 10:
        break
    else:
        print "ENTER A NUMBER BETWEEN 1 AND 10 PLEASE"

num1 = 21

while num != num1:
    num1 = input ("Player 2, guess the number (between 1 and 10): ")
'''

while True:
    print "Who sits in front of me?"
    ans = raw_input (": ")
    
    if ans.upper() == "TONY":
        print "Correct!\n"
        break
    
    else:
        print "Incorrect.\n"
        
while True:
    print "Who sits beside me?"
    ans = raw_input (": ")
    
    if ans.upper() == "DANIEL":
        print "Correct!\n"
        break
    
    else:
        print "Incorrect.\n"
        
while True:
    print "Who sits diagonally from me?"
    ans = raw_input (": ")
    
    if ans.upper() == "JAZIB":
        print "Correct!\n"
        break
    
    else:
        print "Incorrect.\n"
        

        
    
    
    
    
        