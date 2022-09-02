'''
Created on Feb 8, 2018

@author: Luqmaan
'''
import time
import math

while True:
    time.sleep(1)
    print "\nWhich excersise would you like to try?\n\n1 - Distance Calculator\n2 - Name Caser\n3 - Celsius to farenheit\n4 - Field Sizer\n5 - The Box"
    choose = raw_input(": ")
    
    if choose == "1":
        print "Welcome to the Distance Calculator\n"
        cm = raw_input ("Enter the units that your line is in: ")
        print
        print "POINT 1"
        x1 = input ("What does x equal: ")
        y1 = input ("What does y equal: ")
        print
        print "POINT 2"
        x2 = input ("What does x equal: ")
        y2 = input ("What odes y equal: ")
        
        length = "%.2f" %(math.sqrt((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1)))
        print "\nThe length of the line between coordinates ("+str(x1)+","+str(y1)+") and ("+str(x2)+","+str(y2)+") is: "+str(length)+cm
        time.sleep(1)
        
    if choose == "2":
        print "\n"*40
        time.sleep(1)
        
        while True:
            
            name = raw_input ("\nEnter your full name here: ")
        
            if name.count(" ") > 1:
                first = name[0:name.find(" ")]
                last = name[name.rfind(" "):]
                middle = name[name.find(" "):name.rfind(" ")]
                print last+", "+first+middle
                break
            
            elif name.count(" ") == 1:
                first = name[0:name.find(" ")]
                last = name[name.rfind(" "):]
                print last+", "+first
                break
            
            else:
                print "\nPlease put your full name (First name, last name and/or middle name)"
                time.sleep(1)
                
    if choose == "3":
        print "\n"*40
        time.sleep(1)
        c = input ("Enter the celsius: ")
        f = c*9/5+32
        print "\nIt is "+str(c)+" degrees celsius and "+str(f)+" degrees farenheit."
        time.sleep(1)
    
    if choose == "4":
        print "\n"*40
        time.sleep(1)
        
        
        size = input("\nEnter field size: ")
        text = raw_input("Enter text: ")
        
        if int(len(text)) >= size:
            print "\nField size is too small for text!\nYou need a field size of at least "+str(len(text)+2)+" to fit your text!"
            
        else:
            
            star = (int(size) - int(len(text)))/2
            star1 = "*"*star
            star2 = "*"*(star+int(len(text))%2)
            print "\n"+star1+text+star2+"\n"
            
    if choose == "5":
        
        size = input("\nEnter field size: ")
        text = raw_input("Enter text: ")
        
        if int(len(text)) >= size:
            print "\nField size is too small for text!\nYou need a field size of at least "+str(len(text)+2)+" to fit your text!"
            
        else:
            
            star = (int(size) - int(len(text)))/2
            star1 = "*"*(star-1)
            star2 = "*"*(star- 1 +(int(len(text))%2))
            
            box = ("\n"+"*"*size)*((size/2)-1)
            box1 = ("*"*size+"\n")*((size/2+size%2)-2)
            texts = (" "*int((len(text)+2)))
            
            print box
            print star1+texts+star2
            print star1+" "+text+" "+star2
            print star1+texts+star2
            print box1
    
    else:
        pass    
        