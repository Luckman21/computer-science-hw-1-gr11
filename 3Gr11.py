'''
Created on Feb 28, 2018

@author: Luqmaan
'''
from random import randint
import time

while True:
    print "\nWhich program would you like to try?\n\n1 - \"GUESS THE NUMBER\"\n2 - The Fibonacci Sequence\n3 - Common Divisors\n4 - Password Check\n5 - \"VOTE!\"\n\n(0 to quit)"
    choose = raw_input(": ")
    time.sleep(1)
    
    if choose == "1":
        print "\nWelcome to \"GUESS THE NUMBER\", where you must guess the value of a random integer(s) from 0-100."
        start = raw_input ("Press \"ENTER\" to start!")
        a = randint(0,100)  
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
        print "\nHow many numbers of the fibonacci sequence would you like to print out?"
        num = input (": ")
        
        a = 0
        b = 1
        print "\n"+str(a)+" , ",b,", ",
        for x in range (1,(num-3)):
            c = a+b
            print c,", ",
            a = b
            b = c
        c = a+b
        print str(c)+"\n"
        
    elif choose == "3":
        list = [0]
        numb = input ("\nEnter a number: ")
        time.sleep(1)
        num = int(numb)

        if numb > 0:

            for x in range (0,num):
                nums = num%(num-x)
                
                if nums == 0:
                    
                    if list[0] == 0:
                        list[0] = (num-x)
                    else:
                        list.append(num-x)
        
        elif numb < 0:
            num = numb*(-1)
            for x in range (0,num):
                nums = num%(num-x)
                
                if nums == 0:
                    
                    if list[0] == 0:
                        list[0] = (numb+x)
                    else:
                        list.append(numb+x)
    
        else:
            print "\nThe number cannot equal 0!"
            
        if list[0] == 0 and num != 0:
            print "\nThe number "+str(num)+" has no common divisors."
        
        elif list[0] == 0 and num == 0:
            print "\nThe number "+str(num)+" has the common divisor 0."
            
        elif list[0] == 1 and num == 1:
            print "The number "+str(num)+" has the common divisor 1."
        
        else:
            print "\nThe common divisors of "+str(numb)+" are",
            print list
        time.sleep(1)
    
    if choose == "4":
        
        cap = 0
        caps = "QWERTYUIOPASDFGHJKLZXCVBNM"
        num = 0
        nums = "1234567890"
        score = 0
        scores = "_"
        length = 8
        lens = 0
        strength = 0
        
        print "\nWelcome to the password maker!  You can now make your own custom passwords!\nRemember, a strong password contains one capital letter, one number and\ncannot be anything but numbers, letters and underscores \"_\"."
        time.sleep(1)
        code = raw_input("\nEnter you password: ") 
        time.sleep(2)
        
        for abc in code:
            for x in caps:
                if x == abc:
                    cap = 1
            for y in nums:
                if y == abc:
                    num = 1
            for z in scores:
                if z == abc:
                    score = 1
        if len(code) >= 8:
            lens = 1
       
        strength = cap+num+score+lens
        
        if strength == 0:
            per = 0
        else:
            per = (strength*3)-1
        
        for n in range (0,per):
            time.sleep(1)
            print "\n"*50
            print "["+"%"*n+" "*(10-n)+"]"
        time.sleep(0.6)
        
        if strength == 4:
            print "\nStrong Password"
        elif strength == 3:
            print "\nGood Password"
        elif strength == 2:
            print "\nOK Password"
        elif strength == 1:
            print "\nWeak Password"
        else:
            print "\nWell, at this point, you may as well have no password."
        time.sleep(1)
    
    elif choose == "5":
        time.sleep(1)
        print "\nIt's time to... VOTE!"

        tot1 = 0
        tot2 = 0
        tot3 = 0
        vote = 0
        
        while True:
                     
            print "Make a vote for next Prime Minister of Canada:\n\n1 - Osama Bin Laden\n2 - Adolf Hitler\n3 - Donald Trump\n\n(0 to quit)"
            vt = raw_input (": ")
            
            if vt == "1":
                tot1+=1
                vote+=1
                
            elif vt == "2":
                tot2+=1
                vote+=1
            
            elif vt == "3":
                tot3+=1
                vote+=1
                
            elif vt == "0":
                break
            
            else:
                print "\nInvalid Vote.  Please vote again.\n"
                time.sleep(1)
                    
            time.sleep(1)
            
        print "\nHere are the votes:\n"
        time.sleep(1)
        print "Osama Bin Laden - ("+str(tot1)+")"+" ["+str(float(tot1*100/vote))+"%]"
        time.sleep(1)
        print "Adolf Hitler - ("+str(tot2)+")"+" ["+str(float(tot2*100/vote))+"%]"
        time.sleep(1)
        print "Donald Trump - ("+str(tot3)+")"+" ["+str(float(tot3*100/vote))+"%]"+"\n\n"
        time.sleep(1)
        
        if tot1 == tot2 or tot1 == tot3 or tot2 == tot3:
            
            if tot1 == tot2 and tot1 == tot3:
                winner = "It's a tie"
                
            elif tot1 == tot2:
                if tot1 > tot3:
                    winner = "It's a tie"
                    
                else:
                    winner = "Donald Trump"
                    
            elif tot1 == tot3:
                if tot1 > tot2:
                    winner = "It's a tie"
                    
                else:
                    winner = "Adolf Hitler"
                    
            elif tot2 == tot3:
                if tot1 > tot2:
                    winner = "Osama Bin Laden"
                    
                else:
                    winner = "It's a tie"
        
        elif tot1 > tot2 and tot1 > tot3:
            winner = "Osama Bin Laden"
            
        elif tot2 > tot1 and tot2 > tot3:
            winner = "Adolf Hitler"
            
        else:
            winner = "Donald Trump"
        
        time.sleep(1)
        print "The next Prime Minister of Canada is",
        for x in range (0,3):
            print ".",
            time.sleep(1)
        print "\n"+winner+"!\n"
        time.sleep(2)
    
    elif choose == "0":
        print "This is your last chance.  I\'m warning you.  Don't press that button.\n\n1 - Press it\n2 - Don\'t press"
        button = raw_input (": ")
       
        for x in range (0,3):
            print ".",
            time.sleep(1)
            
        if button == "1":
            print "\nYou pressed the button... ;-;"
            time.sleep(1)
            print "Thanks for trying the code."
            break
        else:
            print "\nYou didn\'t press the button??? YAYY!"
            time.sleep(1)
    
    else:
        pass