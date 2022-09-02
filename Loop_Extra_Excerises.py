'''
Created on Mar 19, 2018

@author: Luck
'''
import time
from random import randint

while True:
    print "\nWhich program would you like to try?\n\n1 - \"GUESS THE NUMBER\"\n2 - Even and Odd\n3 - Common Divisors\n4 - Password Check\n5 - \"VOTE!\"\n\n(0 to quit)"
    choose = raw_input(": ")
    time.sleep(1)
    
    if choose == "1":
        print "\nWelcome to \"GUESS THE NUMBER\", where you must guess the value of a random integer(s) from 1-9."
        start = raw_input ("Press \"ENTER\" to start!")
        a = randint(1,9)  
        while True:
            code = input ("\nEnter your guess: ")
            time.sleep(1)
            
            if code > a:
                print "\nToo HIGH!"
                
            elif code < a:
                print "\nToo low :\\"
                
            else:
                break
            
        print "\nYou won!"
        
    elif choose == "2":
        even = ["None"]
        odd  = ["None"]
        
        nums = input ("\nPrint out any sequence of numbers here (use \",\" to space out your numbers): ")
        
        for x in nums:
            if x == 0:
                continue
            
            elif x%2 == 1:
                if odd[0] == "None":
                    odd[0] = x
                else:
                    odd.append(x) 
                    
            else:
                if even[0] == "None":
                    even[0] = x
                else:
                    even.append(x) 
        
        print "\nOdd numbers:",
        print odd
        print "Number of odd numbers: "+str(len(odd))
        print "\nEven numbers:",
        print even
        print "Number of even numbers: "+str(len(even))
    '''
    elif choose == "3":
          