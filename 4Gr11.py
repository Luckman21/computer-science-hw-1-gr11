'''
Created on Mar 26, 2018

@author: Luck
'''
from random import randint
import time

while True:
    time.sleep(1)
    print "\nWhich program would you like to try?\n\n1 - Friendzone\n2 - Bazaar\n3 - Weed\n4 - Lucky Day\n5 - Pythons and Ladders!\n\n(0 to quit)"
    choose = raw_input (": ")
    
    if choose == "0":
        break
    
    elif choose == "1":
        friends,genders,moods = [],[],["loves","hates","kills","kisses","punches"] 
        
        while len(friends) < 5:
            friend = raw_input("\nEnter a name of a friend: ")
            gender = raw_input("\nWhat is their gender?\n\n1 - Male\n2 - Female\n3 - Other\n: ")
            friends.append(friend)
            genders.append(gender)
        
        friend = randint(0,4)
        x,mood = randint(0,4),friends[friend]
        
    elif choose == "2":
        fruits,prices = [],[]
        
        while len(fruits) < 10:
            fruit = raw_input ("Enter a name of a fruit: ")
            price = randint(0,99)
            prices.append(price)
            fruits.append(fruit)
        
        print "\n"+" "*12+"BAZAAR"+"\n"+"-"*33+"\n"+"|"
        for x in range (0,len(fruits)):
            print "| "+str(x+1)+": "+fruits[x]+" - $"+str(prices[x])+".99"
        print"|"+"\n"+"-"*33
  
    elif choose == "3":
        
        count,total,names,weeds = 1,0,[],[]
        
        for x in range (0,8):
            name = raw_input ("Enter a name: ")
            weed = input ("How many weeds did "+name+" pick?\n: ")
            total+=weed

            names.append(name)
            weeds.append(weed)
            
            count+=1
            
        count = 0
        
        for x in weeds: 
            
            if count == 8:
                break   
            
            p = (float(x)/total)*100
            per = '%.2f' % p
            time.sleep(1)
            print "\n"+names[count]+":\n\tNumber of weeds picked: "+str(x)+"\n\tPercentage of weeds picked: "+str(p)+"%\n\tMoney earned: $"+str(per)
            count+=1
            
    elif choose == "4":
        month = ["January","February","March","April","May","June","July","August","September","October","November","December"]
        day28 = []
        day30 = []
        day31 = []
        count = 0
        
        for x in range (1,29):
            day28.append(str(x))
            
        for x in range (1,31):
            day30.append(str(x))
            
        for x in range (1,32):
            day31.append(str(x))
        
        days = [day31,day28,day31,day30,day31,day30,day31,day31,day30,day31,day30,day31] 
        
        for x in days:
            print month[count],x
            count+=1
            
        rmonth = randint(0,11)
        rday = randint(1,len(days[rmonth]))
        
        print "\nYour lucky day is",month[rmonth],days[rmonth][rday]+"!"
    
    elif choose == "5":
        
        title = ["P","Y","T","H","O","N","S"," ","A","N","D"," ","L","A","D","D","E","R","S","!"]
        snake,snakel,ladder,ladderl,space,turn,a = [],[],[],[],[],1,1
        
        time.sleep(1)
        print "\n"*50
        
        for x in title:
            print x,
            time.sleep(0.5)
        
        for x in range (0,11):
            num = randint (13,99)
            for y in range (0,len(snake)):
                if num == snake[y]:
                    num = randint (13,99)
                    num+=3
                else:
                    pass
            snake.append(num)
            
        snake.sort()
            
        for x in range (0,11):
            num = randint (1,88)
            for y in range (0,len(ladder)):
                if num == ladder[y]:
                    num+=3
            for y in range (0,len(snake)):
                if num == snake[y]:
                    num+=3
            ladder.append(num)
            
        ladder.sort()
            
        for x in range (0,11):
            num = randint (7,14)
            snakel.append(num)
            
        for x in range (0,11):
            num = randint (6,12)
            ladderl.append(num)
        
        time.sleep(2)
        print "\n\nWelcome to Pythons and Ladders!\n"
        time.sleep(1)
        name1 = raw_input ("Enter Player 1's name: ")
        time.sleep(1)
        name2 = raw_input ("Enter Player 2's name: ")
        time.sleep(1)
        print "\nNow its time to play!  Now we will randomly select who goes first",
        
        for x in range (0,3):
            print ".",
            time.sleep(1)

        num = randint (1,2)
        
        if num == 1:
            print "\n\nPlayer 1 will start!"
            a = 0
        elif num == 2:
            print "\n\nPlayer 2 will start!"
        
        p1,p2 = name2,name1   
        if a == 0:
            p1,p2 = name1,name2
            
        while space[0] != 100 and space[1] != 100:
            
            time.sleep(1)
            print "\nTURN "+str(turn)+"!"
            print "-"*40,+"\n"
            time.sleep(1)
            
            for x in range (0,2):
                
                if x == 0:
                    p = p1
                else:
                    p = p2
                    
                print "\n"+p+"'s turn!"
                time.sleep(0.4)
               
                while True:   
                    go = raw_input ("\nPress \"ENTER\" key to roll the dice!\n(Press \"0\" and \"ENTER\" to check stats!)\n\n")
                    
                    if go == "":
                        break
                    else:
                        print "\n"+p1+"'s stats:"
                        time.sleep(1)
                        print "Space:",
                        print space[0]
                        print "\n"+p2+"'s stats:"
                        time.sleep(1)
                        print "Space:",
                        print space[1]
                        time.sleep(1)
                        print "\nPythons:",
                        print snake
                        print "Python Lengths:",
                        print snakel
                        time.sleep(1)
                        print "\nLadders:",
                        print ladder
                        print "Ladder Lengths:",
                        print ladderl
                        print "\nTurn#: "+str(turn)
                
                roll = randint (1,6)
                
                if space[x]+roll > 100:
                    print p+" moved 0 spaces because the amount rolled would put you over 100!" 
                    
                else:
                    if roll == 1:
                        print p+" moved 1 space!"
                    else:
                        print p+" moved "+str(roll)+" spaces!"
                    space[x]+=roll
                
                b = 1
                while b == 1:
                    for y in range (0,11):
                        
                        if snake[y] == space[x]:
                            space[x]-=snakel[y]
                            print "You landed on a python on space "+str(snake[y])+"!  You moved back "+str(snakel[y])+" spaces to space "+str(space[x])+"!"
                            break
                        else:
                            b = 0
                    
                    for y in range (0,11):
                        
                        if ladder[y] == space[x]:
                            space[x]+=ladderl[y]
                            print "You landed on a ladder on space "+str(ladder[y])+"!  You moved forward "+str(ladderl[y])+" spaces to space "+str(space[x])+"!"
                            
                        else:
                            b = 0
            
                print p+" is on space "+str(space[x])+"."
                time.sleep(1)
            
            turn+=1
            time.sleep(1)
        
        time.sleep(1)
        print "\n"*50
        time.sleep(1) 
        print "|==========(GAME)==========|"  
        time.sleep(1)
        print "\nStatistics:"
        time.sleep(1)
        print "\n\t"+p1+"'s stats:"
        time.sleep(1)
        print "\t\tSpace:",
        print space[0]
        print "\n\t"+p2+"'s stats:"
        time.sleep(1)
        print "\t\tSpace:",
        print space[1]
        time.sleep(1)
        print "\n\tPythons:",
        print snake
        print "\tPython Lengths:",
        print snakel
        time.sleep(1)
        print "\n\tLadders:",
        print ladder
        print "\tLadder Lengths:",
        print ladderl
        print "\n\tTurn#: "+str(turn-1)
        
        if space[0] == 100 and space[1] == 100:
            print "\nTIE GAME! "+p1+" and "+p2+" both win!"
            
        elif space[0] == 100:
            print "\n"+p1+" wins!\n"
            
        else:
            print "\n"+p2+" wins!\n"