'''
Created on May 1, 2017

@author: Luqmaan
'''
tries = 0
name = raw_input ("Please enter AN APPROPRIATE name: ")

while True:
    
    tries+=1

    num = input ("Enter a number between 1 and 20: ")
      
    if num > 0 and num < 21:
        print "Yay."
        break
    
    elif not (num > 0 and num < 21) and tries == 3:
        print "Please stop being annoying!"
        
    elif not (num > 0 and num < 21) and tries == 5:
        print "I'm warning you!  Please enter the right number!"
        
    elif not (num > 0 and num < 21) and tries == 6:
        print "I've had it with you, "+name+"!"
        break
    
    else:
        print "\n"
    
    