'''
Created on Apr 25, 2017

@author: Luqmaan
'''
y = input ("Enter your year of birth: ")
m = input ("Enter your month of birth: ")
d = input ("Enter your date of birth: ")

if y < 2001:
    print "Older that 16"

elif y >= 2001:
    if m < 4:
        print "Older than 16"
        
    elif m == 4:
        if d < 28:
            print "Older than 16"
            
        if d == 28:
            print "Happy Birthday!"
            
        else:
            print "Younger than 16"
        
    else:
        print "Younger than 16"
        

    