'''
Created on Feb 14, 2018

@author: Luqmaan
'''
from random import randint
import time

while True:
    print "\nWhich part would you like to try?\n\n1 - Part A\t(Beginner)\n2 - Part B\t(Advanced)\n3 - Part C\t(Expert)\n\n(0 end's program and in submenu's exits back to the main menu)"
    choose = raw_input(": ")
    
    if choose == "1":
        print "\nWhich program would you like to try?\n\n1 - Luq's Jersey Shop\n2 - Number Comparison\n3 - Math Test"
        select = raw_input(": ")
        
        if select == "1":
            print "\nHello, welcome to Luq's Jersey Store\n"
            
            while True:
                name = raw_input("\nWhat name would you like on your jersey?\n(Case sensitive)\n: ")
                
                if name == "ABC": #I didn't want to use my own name because I wanted to print my name on the jersey so I used ABC instead
                    print "\nSorry, that name is already taken."
                else:
                    break
            
            num = raw_input("\nWhat number would you like on your jersey?\n(Pick a number between 0-99)\n: ")
            
            if int(num) < 0 or int(num) > 99:
                print "\nSorry, that number is not available"
            
            else:
                
                side1 = ((10 - len(num))/2)-1+(len(num)%2)
                side2 = ((10 - len(num))/2)
                sides1 = ((10 - len(name))/2)-1+(len(name)%2)
                sides2 = ((10 - len(name))/2)
                print "Here is your jersey:"
                time.sleep(1)
                
                print "   _     _"
                print " _| |___| |_"
                print "_)         (_"
                print "||"+" "*(sides1)+name+" "*(sides2)+"||"
                print "||         ||"
                print "||"+" "*(side1)+num+" "*(side2)+"||"
                print "||         ||"
                print "||         ||"
                print "||         ||"
                print "||_________||"
        
        elif select == "2":
            print "\nWelcome to: \"The Bigger Digit\"\n\nOn this show, we let the player enter either 2 numbers or 1 number.\nOur program will then decide which number is greater.  Are you ready?"
            time.sleep(1)
            sel = raw_input("\nWhich would you like to do?\n\n1 - 1 Number\n2 - 2 Numbers\n: ")
            
            if sel == "1":
                num1 = input("\nEnter a number: ")
                num2 = randint(0,100000)
                
            else:
                num1 = input("\nEnter a number: ")
                num2 = input("\nEnter a number: ")
                
            if num1 > num2:
                print "Number 1 ("+str(num1)+") is greater than Number 2 ("+str(num2)+")!"
                
            elif num1 == num2:
                print "Ha!  You cant fool me!  Both Number 1 ("+str(num1)+") and Number 2 ("+str(num2)+") are the same number!"
                
            else:
                print "Number 2 ("+str(num2)+") is greater than Number 1 ("+str(num1)+")!"
        
        elif select == "3":
            print "\nOk everyone.  Close your books and keep only a pencil and eraser on your desk, because you're gonna need it!"
            time.sleep(1)
            print "Can you ace this math test without studying?  Let's find out!"
            name = raw_input("\nName: ")
            date = raw_input("Date: ")
            time.sleep(1)
            print "\n"*40
            point = 0
            
            for x in range (1,4):
                print "\n-----Question #"+str(x)+"-----\n"
                num1 = randint(0,100000000)
                num2 = randint(1,100000000)
                op = randint(1,4)
                
                if op == 1:
                    test = input(str(num1)+" + "+str(num2)+" = ")
                    ans = num1+num2
                    
                elif op == 2:
                    test = input(str(num1)+" - "+str(num2)+" = ")
                    ans = num1-num2
                    
                elif op == 3:
                    test = input(str(num1)+" x "+str(num2)+" = ")
                    ans = num1*num2
                    
                elif op == 4:
                    test = input(str(num1)+" / "+str(num2)+" = ")
                    ans = num1/num2
                    
                if test == ans:
                    time.sleep(1)
                    print "\nYou are..."
                    time.sleep(1)
                    print "Correct!"
                    point+=1
                
                else:
                    time.sleep(1)
                    print "\nSorry, that was incorrect."
                    time.sleep(1)
                    print "Here is the correct answer: "+str(ans)
                    
            if point == 1 or point == 0:
                mark = "F"
                msg = "\nOuch.  Don't worry, you will do better next time!"
            elif point == 2:
                mark = "C"
                msg = "\nNice try!  Not quite an A, but still passing!"
            else:
                mark = "A+"
                msg = "\nAmazing job!  You deserve a medal!"
            print "\nThe results are in.  Let's take a look at your test score!\n\n"
            time.sleep(1)
            print "Name: "+name
            print "Date: "+date
            time.sleep(1)
            print "\nPoints: "+str(point)+"/3"
            time.sleep(1)
            print "Score: "+str(point/3)+"%"
            time.sleep(1)
            print "Mark: "+mark
            print "\nCome back next time for a new challenge!"
            time.sleep(2)
    
    if choose == "2":
        print "\nWhich program would you like to try?\n\n1 - Country Trivia\n2 - Smallest Number\n3 - Largest Number\n4 - Age Definer\n5 - Rock, Paper, Scissors\n6 - Language Greeter\n7 - Leftovers"
        select = raw_input(": ")
        
        if select == "1":
        
            print "\nWelcome to Country Trivia!\n"
            country = raw_input ("What country are you from?:")
            country1 = country.upper()
            
            if country1 == "CANADA":
                print "\nCool!\n\"Oh Canada!  We stand on guard for thee...\""
                time.sleep(1)
                countryans1 = raw_input ("What is that from?: ").upper()
                
                if countryans1 == "NATIONAL ANTHEM" or countryans1 == "NATIONAL ANTHEM OF CANADA" or countryans1 == "CANADA'S NATIONAL ANTHEM":
                    print "\nCorrect!\n"
                    
                else:
                    print "\nNice try!\n"
                    
                
            elif country1 == "USA":
                print "Cool! \nI am going to make America great again!"
                countryans = raw_input ("Who said that?: ")
                countryans1 = countryans.upper()
                
                if countryans1 == "DONALD TRUMP":
                    print "\nCorrect!\n"
                    
                else:
                    print "\nNice try!\n"
                
            elif country1 == "CHINA":
                print "Cool!\n\"Ni Hao\"!  Do you know what that means?"
                countryans = raw_input ("Guess: ")
                countryans1 = countryans.upper()
                
                if countryans1 == "HELLO":
                    print "\nCorrect!\n"
                    
                else:
                    print "\nNice try!\n"
                
                
            else:
                print "\nCool!  I don't really know much about that country, but feel free to tell me a bit about it!"
                countryinfo = raw_input (": ")       
                
        elif select == "2":
            print "Welcome to \"Smallest Number!\""
            num1 = input ("Type in number 1: ")
            num2 = input ("Type in number 2: ")
            num3 = input ("Type in number 3: ")
            print
            
            if num1 < num2:
                if num1 < num3:
                    print "Number 1 ("+str(num1)+") is the smallest."
                else:
                    print "Number 3 ("+str(num3)+") is the smallest."
                    
            elif num2 < num1:
                if num2 < num3:
                    print "Number 2 ("+str(num2)+") is the smallest."
                else:
                    print "Number 3 ("+str(num3)+") is the smallest."
                    
            elif num3 < num1:
                if num3 < num2:
                    print "Number 3 ("+str(num3)+") is the smallest."
                else:
                    print "Number 2 ("+str(num2)+") is the smallest."
                
            else:
                print "Next time, don't print numbers with the same value!!!"
        
        elif select == "3":
            print "Welcome to \"Largest Number!\""
            num1 = input ("Type in number 1: ")
            num2 = input ("Type in number 2: ")
            num3 = input ("Type in number 3: ")
            print
            
            if num1 > num2:
                if num1 > num3:
                    print "Number 1 ("+str(num1)+") is the greatest."
                else:
                    print "Number 3 ("+str(num3)+") is the greatest."
                    
            elif num2 > num1:
                if num2 > num3:
                    print "Number 2 ("+str(num2)+") is the greatest."
                else:
                    print "Number 3 ("+str(num3)+") is the greatest."
                    
            elif num3 > num1:
                if num3 > num2:
                    print "Number 3 ("+str(num3)+") is the greatest."
                else:
                    print "Number 2 ("+str(num2)+") is the greater."
                
            else:
                print "Next time, don't print numbers with the same value!!!"
        
        elif select == "4":
            print "\nWhat is your age?"
            age = raw_input (": ")
            print
            
            if age < 0:
                print "Are you even born yet?"
            elif age < 13:
                print "You are a child.  Go play with your toys."
            elif age >= 13 and age <= 19:
                print "You are a teen.  Stop looking at your phone and look at the code."
            elif age >= 20 and age <=65:
                print "You are an adult.  What are you doing with your life?"
            elif age > 65:
                print "You are a senior citizen.  Go enjoy what's left of your life."
        
        elif select == "5":
            print "\nWelcome to \"Rock, Paper, Scissors!\""
            name = raw_input ("\nPlease enter your full name here: ")
            
            name1 = name.count(" ")
            
            if name1 >= 1:
                name2 = name[0:name.find(" ")]
                name = name2
            
            else:
                name = name
                
            print "\nHello, "+name+"."
            
            while True:
                
                rounds = input ("\nHow many rounds do you want to play?: ")
                
                round1 = 0
                point = 0
                pointd = 0
                
                while round1 < rounds:
                    
                    round1+=1
                    
                    rpsd = randint (1,3)
                    
                    print "\nROUND "+str(round1)
                    print "-"*40
                    
                    print "\n1 - Rock\n2 - Paper\n3 - Scissors"
                    rps = input (": ")
                    time.sleep(1)
                    print
                    
                    if rps == 1:
                        
                        if rpsd == 1:
                            print "You chose Rock!"
                            time.sleep(1)
                            print "The Python chose Rock!"
                            time.sleep(1)
                            print "Score: \n\t"+name+": "+str(point)+"\n\tThe Python: "+str(pointd)
                            time.sleep(1)
                            
                        elif rpsd == 2:
                            print "You chose Rock!"
                            time.sleep(1)
                            print "The Python chose Paper!"
                            time.sleep(1)
                            pointd+=1
                            print "Score: \n\t"+name+": "+str(point)+"\n\tThe Python: "+str(pointd)
                            time.sleep(1)
                    
                        elif rpsd == 3:
                            print "You chose Rock!"
                            time.sleep(1)
                            print "The Python chose Scissors!"
                            time.sleep(1)
                            point+=1
                            print "Score: \n\t"+name+": "+str(point)+"\n\tThe Python: "+str(pointd)
                            time.sleep(1)
                            
                    elif rps == 2:
                        
                        if rpsd == 1:
                            print "You chose Paper!"
                            time.sleep(1)
                            print "The Python chose Rock!"
                            time.sleep(1)
                            point+=1
                            print "Score: \n\t"+name+": "+str(point)+"\n\tThe Python: "+str(pointd)
                            time.sleep(1)
                            
                        elif rpsd == 2:
                            print "You chose Paper!"
                            time.sleep(1)
                            print "The Python chose Paper!"
                            time.sleep(1)
                            print "Score: \n\t"+name+": "+str(point)+"\n\tThe Python: "+str(pointd)
                            time.sleep(1)
                    
                        elif rpsd == 3:
                            print "You chose Paper!"
                            time.sleep(1)
                            print "The Python chose Scissors!"
                            time.sleep(1)
                            pointd+=1
                            print "Score: \n\t"+name+": "+str(point)+"\n\tThe Python: "+str(pointd)
                            time.sleep(1)
                            
                    elif rps == 3:
                        
                        if rpsd == 1:
                            print "You chose Scissors!"
                            time.sleep(1)
                            print "The Python chose Rock!"
                            time.sleep(1)
                            pointd+=1
                            print "Score: \n\t"+name+": "+str(point)+"\n\tThe Python: "+str(pointd)
                            time.sleep(1)
                            
                        elif rpsd == 2:
                            print "You chose Scissors!"
                            time.sleep(1)
                            print "The Python chose Paper!"
                            time.sleep(1)
                            point+=1
                            print "Score: \n\t"+name+": "+str(point)+"\n\tThe Python: "+str(pointd)
                            time.sleep(1)
                    
                        elif rpsd == 3:
                            print "You chose Scissors!"
                            time.sleep(1)
                            print "The Python chose Scissors!"
                            time.sleep(1)
                            print "Score: \n\t"+name+": "+str(point)+"\n\tThe Python: "+str(pointd)
                            time.sleep(1)
                    
                    else:
                        print "("+str(rps)+") is not a proper command, so you lost that round!"
                        pointd+=1
                        time.sleep(2)
                        print "\nHere is the score:\n\n\t"+name+": "+str(point)+"\n\tThe Python: "+str(pointd)+"\n\tRounds Played: "+str(rounds)
                        time.sleep(1)
                        
                if point > pointd:
                    print "\nYou won! :)\n"  
                    
                elif point == pointd:
                    print "\nTie game! :|\n"
                    
                else:
                    print "\nYou lost! :(\n"
                    
                print
                time.sleep(1)
                print "Do you want to play again?\n\n1 - Yes\n2 - No"
                a = input (": ")
                
                if a == 2:
                    print "\nYou didn't want to play again... :("
                    break
                    
                else:
                    print "\nYou wanted to play again! :)"
                        
        elif select == "6":      
            print "\nWelcome to the \"Language Greeter\"!\n"
            print "Choose your language:\n\n1 - English\n2 - French\n3 - Spanish"
            choose = raw_input (": ")
            
            if choose == "1":
                print "Hello!"
                
            elif choose == "2":
                print "Bonjour!"
                
            elif choose == "3":
                print "Hola!"
                
            else:
                print "Sorry, that was not a language option..."  
                
        elif select == "7":
            print "\nWelcome to Leftovers.  The aim of the game is to enter 2 numbers.  You must then guess the remainder of the 2.  \nIf you get it right, you win!  Ready to play?" 
            enter = raw_input ("Press \"ENTER\" to start!")
            print "\n"*50
            time.sleep(1)
            
            num1 = input ("\nEnter the first number: ")
            num2  = input ("\nEnter the second number: ")
            
            ans = num1%num2
            
            answer = input("\nWhat is the remainder of "+str(num1)+" and "+str(num2)+"?\n: ")
            time.sleep(1)
            if ans == answer:
                print "\nCorrect!"  
            else:
                print "\nRemember, the modulo gets the remainder of the number."
    
    if choose == "3":
        print "\nWhich program would you like to try?\n\n1 - Number Orderer\n2 - Solutions of the Function\n3 - Largest Number\n4 - Pocket Change"
        select = raw_input (": ")
        if select == "1":
            print "\nWelcome to the number orderer.  Enter 3 values and the code will rearrange them in ascending order!\n"
            num1 = input ("Enter value 1: ")
            num2 = input ("Enter value 2: ")
            num3 = input ("Enter value 3: ")
            a,b,c = 0,0,0
            
            if num1 == num2 or num1 == num3 or num2 == num3:
                if num1 == num2 and num1 == num3:
                    a = num1
                    b = num1
                    c = num1
                    
                elif num1 == num2:
                    if num1 > num3:
                        a = num1
                        b = num1
                        c = num3 
                    else:
                        a = num3
                        b = num1
                        c = num1
                        
                elif num1 == num3:
                    if num1 > num2:
                        a = num1
                        b = num1
                        c = num2  
                    else:
                        a = num2
                        b = num1
                        c = num1 
                        
                else:
                    if num2 > num1:
                        a = num2
                        b = num2
                        c = num1  
                    else:
                        a = num1
                        b = num2
                        c = num2
            
            if num1 > num2:
                if num1 > num3:
                    if num2 > num3:
                        a = num1
                        b = num2
                        c = num3
                        
                    else:
                        a = num1
                        b = num3
                        c = num2
            
            if num2 > num1:
                if num2 > num3:
                    if num1 > num3:
                        a = num2
                        b = num1
                        c = num3
                    else:
                        a = num2
                        b = num3
                        c = num1
                        
            if num3 > num1:
                if num3 > num2:
                    if num2 > num1:
                        a = num3
                        b = num2
                        c = num1
                    else:
                        a = num3
                        b = num1
                        c = num2   
            
            print "\nHere is the order: "+str(c)+", "+str(b)+", "+str(a)
                
        if select == "2":
            #x = (-b+/-(b**2-4*a*c)**(1/2))/2*a*c    
            #y = (a)(x**2)+(b)(x)+c
            print "\nWelcome to \"Solutions of a Function\" program, where you input the numbers and we solve for the x intercepts!\n"
            time.sleep(1)
            a = input ("Enter your \'a\' value: ")
            b = input ("Enter your \'b\' value: ")
            c = input ("Enter your \'c\' value: ")
            
            a = float(a)
            b = float(b)
            c = float(c)
            
            time.sleep(1)
            print "\nYour quadratic Formula in standard form:\n\n"+str(a)+"x^2 + "+str(b)+"x + "+str(c)
            print
            time.sleep(1)
            
            dis = (b**2) - (4*a*c)
            print "\nDiscriminant: "+str(dis)
            
            if dis > 0:
                print "The function has more than one solution."
                time.sleep(1)
                
                x = ((b**2)-(4*a*c))**(0.5)
                x1 = (((-1.0)*b) + x)/(2*a)
                x2 = (((-1.0)*b) - x)/(2*a)
                
                print "\nThe solutions of this function are x = "+str(x1)+" and x = "+str(x2)+"."
                time.sleep(1)
                
            elif dis == 0:
                print "The function has 1 solution."
                time.sleep(1)
                
                x = ((-1)*b)/(2*a*c)
                
                print "\nThe solution of the function is x = "+str(x)+"."
                
            else:
                print "The function has no solutions."
                time.sleep(1)
                
        if select == "3":
            time.sleep(1)
            mass = input ("\nEnter the mass of your letters (in grams)\n: ")
            sina = 0
            
            if mass <= 30:
                sina = 40
            elif mass > 30 and mass <= 50:
                sina = 55
            elif mass > 50 and mass <= 100:
                sina = 70
            else:
                sina = 70
                while mass > 100.0:
                    sina+=25
                    mass-=50
                    
            time.sleep(0.5)
            print "The cost is "+str(sina)+" sinas."
            time.sleep(1)
                    
                    
        if select == "4":
            print "\n\"POCKET CHANGE\""
            print "\nWhat's the most efficient way to carry your spare change?\n"
            cash = input ("Enter value of change (in dollars): $")
            change = float(cash)
            print change
            time.sleep(1)
            toon,loon,quart,dime,nick,pen = 0,0,0,0,0,0
            
            while True:
                if change == 0.00:
                    break
                elif change >= 2.00:
                    toon+=1
                    change-=2.00
                elif change >= 1.00:
                    loon+=1
                    change-=1.00
                elif change >= 0.25:
                    quart+=1
                    change-=0.25
                elif change >= 0.1:
                    dime+=1
                    change-=0.10
                elif change >= 0.05:
                    nick+=1
                    change-=0.05
                elif change >= 0.01:
                    pen+=1
                    change-=0.01
                print toon,loon,quart,dime,nick,pen
                print change
                  
            if toon == 1:
                toons = "toonie"
            else:
                toons = "toonies"
            if loon == 1:
                loons = "loonie"
            else:
                loons = "loonies"
            if quart == 1:
                quarts = "quarter"
            else:
                quarts = "quarters"
            if dime == 1:
                dimes = "dime"
            else:
                dimes = "dimes"
            if nick == 1:
                nicks = "nickel"
            else:
                nicks = "nickels"
            if pen == 1:
                pens = "penny"
            else:
                pens = "pennies"
                
            print "To carry the least amount of change, bring "+str(toon)+" "+toons+", "+str(loon)+" "+loons+", "+str(quart)+" "+quarts+", "+str(dime)+" "+dimes+", "+str(nick)+", "+nicks+" and "+str(pen)+" "+pens+"."
            #print "To carry the least amount of change, bring "+str(quart)+" "+quarts+", "+str(dime)+" "+dimes+", "+str(nick)+", "+nicks+" and "+str(pen)+" "+pens+"."
  
    if choose == "0":
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