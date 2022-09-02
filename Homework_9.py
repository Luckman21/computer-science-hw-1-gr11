'''
Created on Apr 20, 2017

@author: Luqmaan
'''

from random import randint
import time

a = 1

while a == 1:

        time.sleep(1)
        print "\nChoose which types of programs you want to try:"
        time.sleep(1)
        print "\nChoose the program you want to run by entering the number to the left of it and pressing enter.\n"
        time.sleep(1)
        print "1 - A (Beginner)"
        time.sleep(1)
        print "2 - B (Advanced)"
        time.sleep(1)
        print "3 - C (Expert)"
        time.sleep(1)
        b = input (": ")
        time.sleep(1)
            
        if b == 1: #PART 1
            print "\nChoose the program you want to run by entering the number to the left of it and pressing enter.\n"
            time.sleep(1)
            print "1 - Same Name?"
            time.sleep(1)
            print "2 - Biggest Number!"
            time.sleep(1)
            print "3 - Math Test"
            time.sleep(1)
            c = input (": ")
            
            if c == 1:
                
                print "\nWelcome to the \"Same Name?\" program\n"
                name = raw_input ("Please enter your name: ")

                if name == "Luqmaan Irshad":
                    print "HEY THATS MY NAME!"
                    
                else:
                    print "Hello, "+name
                        
            elif c == 2:
                print "Welcome to the \"Biggest Number!\"program"
                num1 = input ("Type in number 1: ")
                num2 = input ("Type in number 2: ")
                
                if num1 > num2:
                    print "Number 1 ("+str(num1)+") is greater than number 2 ("+str(num2)+")"
                
                elif num2 > num1:
                    print "Number 2 ("+str(num2)+") is greater than number 1 ("+str(num1)+")"
                    
                elif num1 == num2:
                    print "Number 1("+str(num1)+")is equal to number 2("+str(num2)+")"
            
            elif c == 3:
                mark = 0
                print "\nWelcome to the \"Math Test\"!\n"
                time.sleep(1)
                print "Solve these 3 math problems:"
                time.sleep(1)
                q1 = input ("34.5 x 2 = ")
                time.sleep(1)
                print "356 - X = -64"
                q2 = input ("X = ")
                time.sleep(1)
                q3 = input ("9 + 10 =  ")
                
                if 69 == q1:
                    mark+=1
                    q1 = "right"
                else:
                    mark+=0
                    q1 = "wrong (ans = 69)"
                    
                if 420 == q2:
                    mark+=1
                    q2 = "right"
                else:
                    mark+=0
                    q2 = "wrong (ans = 420)"
                    
                if 19 == q3:
                    mark+=1
                    q3 = "right"
                else:
                    mark+=0
                    q3 = "wrong (ans = 19)"
                    
                time.sleep(1)
                print "You got question 1 "+q1+", question 2 "+q2+" and question 3 "+q3
                time.sleep(2)
                print "Your mark is: "+str((mark/3.0)*100)+"%"
            
            else:
                c = randint (1,3)
                if c == 1:
                
                    print "\nWelcome to the \"Same Name?\" program\n"
                    name = raw_input ("Please enter your name: ")
    
                    if name == "Luqmaan Irshad":
                        print "HEY THATS MY NAME!"
                        
                    else:
                        print "Hello, "+name
                            
                elif c == 2:
                    print "Welcome to the \"Biggest Number!\"program"
                    num1 = input ("Type in number 1: ")
                    num2 = input ("Type in number 2: ")
                    
                    if num1 > num2:
                        print "Number 1 ("+str(num1)+") is greater than number 2 ("+str(num2)+")"
                    
                    elif num2 > num1:
                        print "Number 2 ("+str(num2)+") is greater than number 1 ("+str(num1)+")"
                        
                    elif num1 == num2:
                        print "Number 1("+str(num1)+")is equal to number 2("+str(num2)+")"
                
                elif c == 3:
                    mark = 0
                    print "\nWelcome to the \"Math Test\"!\n"
                    time.sleep(1)
                    print "Solve these 3 math problems:"
                    time.sleep(1)
                    q1 = input ("34.5 x 2 = ")
                    time.sleep(1)
                    print "356 - X = -64"
                    q2 = input ("X = ")
                    time.sleep(1)
                    q3 = input ("9 + 10 =  ")
                    
                    if 69 == q1:
                        mark+=1
                        q1 = "right"
                    else:
                        mark+=0
                        q1 = "wrong (ans = 69)"
                        
                    if 420 == q2:
                        mark+=1
                        q2 = "right"
                    else:
                        mark+=0
                        q2 = "wrong (ans = 420)"
                        
                    if 19 == q3:
                        mark+=1
                        q3 = "right"
                    else:
                        mark+=0
                        q3 = "wrong (ans = 19)"
                        
                    time.sleep(1)
                    print "You got question 1 "+q1+", question 2 "+q2+" and question 3 "+q3
                    time.sleep(2)
                    print "Your mark is: "+str((mark/3.0)*100)+"%"

            
        elif b == 2: #PART 2
            print "\nChoose the program you want to run by entering the number to the left of it and pressing enter.\n"
            time.sleep(1)
            print "1 - Country Trivia"
            time.sleep(1)
            print "2 - Smallest Number!"
            time.sleep(1)
            print "3 - Biggest Number 2!"
            time.sleep(1)
            print "4 - Age Grouper"
            time.sleep(1)
            print "5 - Rock, Paper, Scissors!"
            time.sleep(1)
            print "6 - Language Greeter"
            time.sleep(1)
            print "7 - Number Guessing Game!"
            time.sleep(1)
            c = input (": ")
            
            if c == 1:
                print "\nWelcome to Country Trivia!\n"
                country = raw_input ("What country are you from?:")
                country1 = country.upper()
                
                if country1 == "CANADA":
                    print "\nCool!\n\"Oh Canada!  We stand on guard for thee...\""
                    time.sleep(1)
                    countryans = raw_input ("What is that from?: ")
                    countryans1 = countryans.upper()
                    
                    if countryans1 == "NATIONAL ANTHEM":
                        print "\nCorrect!\n"
                        
                    elif countryans1 == "NATIONAL ANTHEM OF CANADA":
                        print "\nCorrect!\n"
                        
                    elif countryans1 == "CANADA'S NATIONAL ANTHEM":
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
        
            elif c == 2:
                print "Welcome to \"Smallest Number!\""
                num1 = input ("Type in number 1: ")
                num2 = input ("Type in number 2: ")
                num3 = input ("Type in number 3: ")
                
                if num1 < num2 and num1 < num3:
                    print "Number 1 ("+str(num1)+") is the smallest."
                
                elif num2 < num1 and num2 < num3:
                    print "Number 2 ("+str(num2)+") is the smallest."
                    
                elif num3 < num1 and num3 < num2:
                    print "Number 1("+str(num1)+")is equal to number 2("+str(num2)+")"
                    
                else:
                    print "Next time, don't print numbers with the same value!!!"
                    
            elif c == 3:
                print "Welcome to \"Biggest Number 2!\""
                num1 = input ("Type in number 1: ")
                num2 = input ("Type in number 2: ")
                num3 = input ("Type in number 3: ")
                
                if num1 >= num2:
                    if num1 > num3:
                        if num1 == num2:
                            print "Number 1 (", num1 ,") and number 2 (", num2 ,") are the biggest"
                        else:
                            print "Number 1(", num1 ,") is the biggest."
                    else:
                        print "Number 3 (", num3 ,") is the biggest."
                        
                elif num2 >= num3:
                    if num2 > num3:
                        print "Number 2 (", num2 ,") is the biggest."
                    else:
                        print "Number 2 (", num2 ,") and number 3 (", num3 ," are the biggest."
                        
                elif num1 == num2 and num1 == num3:
                    print "All 3 numbers are the same! (", num1 ,")"
                    
                else:
                    print "Number 3 (", num3 ,") is the biggest."
                    
            elif c == 4:
                print "\nWelcome to the \"Age Grouper\"!\n"
                age = input ("Please enter your age here: ")
                
                if age < 13 and age > 0:
                    print "You are ",age," years old, and you are a child."
                    
                elif age > 12 and age < 20:
                    print "You are ",age," years old, and you are a teenager."
                    
                elif age > 18 and age < 65:
                    print "You are ",age," years old, and you are an adult."
                    
                elif age < 0:
                    print "You are ",age," years old.  Are you even born yet???"
                    
                else:
                    print "You are ",age," years old, and you are a senior."
                    
            elif c == 5:
                print "\nWelcome to \"Rock, Paper, Scissors!\""
                round = input ("How many rounds do you want to play?: ")
                
                round1 = 0
                point = 0
                pointd = 0
                
                while round1 < round:
                    
                    round1+=1
                    
                    rpsd = randint (1,3)
                    
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
                            print "Score: \n\tYou: "+str(point)+"\n\tThe Python: "+str(pointd)
                            time.sleep(1)
                            
                        elif rpsd == 2:
                            print "You chose Rock!"
                            time.sleep(1)
                            print "The Python chose Paper!"
                            time.sleep(1)
                            pointd+=1
                            print "Score: \n\tYou: "+str(point)+"\n\tThe Python: "+str(pointd)
                            time.sleep(1)
                    
                        elif rpsd == 3:
                            print "You chose Rock!"
                            time.sleep(1)
                            print "The Python chose Scissors!"
                            time.sleep(1)
                            point+=1
                            print "Score: \n\tYou: "+str(point)+"\n\tThe Python: "+str(pointd)
                            time.sleep(1)
                            
                    elif rps == 2:
                        
                        if rpsd == 1:
                            print "You chose Paper!"
                            time.sleep(1)
                            print "The Python chose Rock!"
                            time.sleep(1)
                            point+=1
                            print "Score: \n\tYou: "+str(point)+"\n\tThe Python: "+str(pointd)
                            time.sleep(1)
                            
                        elif rpsd == 2:
                            print "You chose Paper!"
                            time.sleep(1)
                            print "The Python chose Paper!"
                            time.sleep(1)
                            print "Score: \n\tYou: "+str(point)+"\n\tThe Python: "+str(pointd)
                            time.sleep(1)
                    
                        elif rpsd == 3:
                            print "You chose Paper!"
                            time.sleep(1)
                            print "The Python chose Scissors!"
                            time.sleep(1)
                            pointd+=1
                            print "Score: \n\tYou: "+str(point)+"\n\tThe Python: "+str(pointd)
                            time.sleep(1)
                            
                    elif rps == 3:
                        
                        if rpsd == 1:
                            print "You chose Scissors!"
                            time.sleep(1)
                            print "The Python chose Rock!"
                            time.sleep(1)
                            pointd+=1
                            print "Score: \n\tYou: "+str(point)+"\n\tThe Python: "+str(pointd)
                            time.sleep(1)
                            
                        elif rpsd == 2:
                            print "You chose Scissors!"
                            time.sleep(1)
                            print "The Python chose Paper!"
                            time.sleep(1)
                            point+=1
                            print "Score: \n\tYou: "+str(point)+"\n\tThe Python: "+str(pointd)
                            time.sleep(1)
                    
                        elif rpsd == 3:
                            print "You chose Scissors!"
                            time.sleep(1)
                            print "The Python chose Scissors!"
                            time.sleep(1)
                            print "Score: \n\tYou: "+str(point)+"\n\tThe Python: "+str(pointd)
                            time.sleep(1)
                    
                    else:
                        print "("+str(rps)+") is not a proper command, so you lost that round!"
                        pointd+=1
                
                time.sleep(2)
                print "Here is the score:\n\tYou: "+str(point)+"\n\tThe Python: "+str(pointd)+"\n\tRounds Played: "+str(round)
                time.sleep(1)
                
                if point > pointd:
                    print "\nYou won! :)\n"  
                    
                elif point == pointd:
                    print "\nTie game! :|\n"
                    
                else:
                    print "\nYou lost! :(\n"                    
                    
            elif c == 6:
                print "\nWelcome to the \"Language Greeter\"!\n"
                print "Choose your language:\n\n1 - English\n2 - French\n3 - Spanish"
                choose = raw_input (": ")
                
                if choose == 1:
                    print "Hello!"
                    
                elif choose == 2:
                    print "Bonjour!"
                    
                elif choose == 3:
                    print "Hola!"
                    
                else:
                    print "Sorry, that was not a language option..."
                    
            elif c == 7:
                print "\nWelcome to the \"Number Guessing Game!\"\n"
                print "Choose 2 numbers (out of 100)"
                num1 = input ("Number 1: ")
                num2 = input ("Number 2: ")
                
                numb1 = randint (1,100)
                numb2 = randint (1,100)
                
                print "\n"+str(numb1)+"\n"+str(numb2)+"\n"
                
                if num1 == numb1 or num1 == numb2:
                    if num1 == numb1 and num1 == numb2:
                        if num1 == num2:
                            print "WOW, ALL THE NUMBERS ARE THE SAME!!!\nYOU MIGHT WANT TO TAKE A PICTURE, BECAUSE THIS IS A VERY RARE OCCURANCE!"
                        else:
                            print "That's AMAZING!  You might want to take a picture because this doesn't happen too often..."
                    elif num1 == numb1:
                        if num1 == num2:
                            print "Wow, that's great!  The numbers you entered are the same, and they match one of the random numbers!"
                        else:
                            print "Cool!  One of your numbers matches the random numbers!"
                    elif num1 == numb2:
                        if num1 == num2:
                            print "Wow, that's great!  The numbers you entered are the same, and they match one of the random numbers!"
                        else:
                            print "Cool!  One of your numbers matches the random numbers!"
                    
                elif num2 == numb1 or num2 == numb2:
                    if num2 == numb1 and num2 == numb2:
                        if num1 == num2:
                            print "WOW, ALL THE NUMBERS ARE THE SAME!!!\nYOU MIGHT WANT TO TAKE A PICTURE, BECAUSE THIS IS A VERY RARE OCCURANCE!"
                        else:
                            print "That's AMAZING!  You might want to take a picture because this doesn't happen too often..."
                    elif num2 == numb1:
                        if num1 == num2:
                            print "Wow, that's great!  The numbers you entered are the same, and they match one of the random numbers!"
                        else:
                            print "Cool!  One of your numbers matches the random numbers!"
                    elif num2 == numb2:
                        if num1 == num2:
                            print "Wow, that's great!  The numbers you entered are the same, and they match one of the random numbers!"
                        else:
                            print "Cool!  One of your numbers matches the random numbers!"
                            
                elif num1 == num2:
                    print "Only the numbers you entered matched."
                    
                else:
                    print "None of the numbers you entered matched..."


'''                        
            
            
        elif b == 3:#PART 3
            print "\nChoose the program you want to run by entering the number to the left of it and pressing enter.\n"
            time.sleep(1)
            print "1 - Same Name?"
            time.sleep(1)
            print "2 - "
            time.sleep(1)
            print "3 - "
            time.sleep(1)
            print "4 - "
            
        else:
            b = randint (1,3)

time.sleep(1)
print "\nDo you want to try another program?\n"
time.sleep(1)
print "1 - Yes"
time.sleep(1)
print "2 - No"
time.sleep(1)
a = input (": ")

if a == 2:
    print "You didn't want to try another program... :("
else:
    print "You wanted to try another program! :)"
    
    
    
'''
