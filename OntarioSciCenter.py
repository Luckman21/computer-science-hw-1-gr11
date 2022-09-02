'''
Created on Feb 13, 2018

@author: Luqmaan
'''
import time
cost = []
tick = []
money = 0

time.sleep(1)
print "Welcome to the Ticket Booker.  Please enter the number of tickets you would like to purchase"
ppl = input(": ")

for x in range(ppl):
    time.sleep(1)
    print "\n|----TICKET #"+str(x+1)+"----|"
    print "How old is the person you are purchasing the ticket for?"
    age = input(": ")
    time.sleep(1)
    
    if age <= 2:
        print "\nThe ticket you are purchasing is \"FREE\""
        cost.append(0.0)
        tick.append("\t(GOLD)")
    
    else:
        print "\nAre you an Ontario Science Center Member?"
        member = raw_input("\n1 - Yes\n2 - No\n: ")
        time.sleep(1)
        
        if member == "1":
            print "\nThe ticket you are purchasing is \"FREE\""
            cost.append(0.0)
            tick.append("\t(GOLD)")
            
        else:
            print "\nAre you a student with ID?\n\n1 - Yes\n2 - No"
            eyeD = raw_input(": ")
            
            
            if age >= 18 and age <=64:
                dis = 7.00
                gold = 28.00
                silver = 22.00
                bronze = 13.00
            else:
                if age >= 13 and age <= 17 or age >= 65 or eyeD == "1":
                    gold = 22.00
                    silver = 16.00
                    bronze = 9.00
                    
                if age >= 3 and age <= 12:
                    gold = 19.00
                    silver = 13.00
                    bronze = 9.00
                dis = 3.00
                
            print "\nWhich ticket are you purchasing?\n\n1 - Imax + Science Center (GOLD)\tSave $"+str(dis)+"\n\t$"+str(gold)+"\n2 - Science Center (SILVER)\n\t"+str(silver)+"\n3 - Imax (BRONZE)\n\t"+str(bronze)
            print "\nTax not included\n"
            ticket = raw_input(": ")
            
            if ticket == "1": #or ticket.upper == "GOLD":
                a = gold-dis
                b = "\t(GOLD)"
            elif ticket == "2": #or ticket.upper == "SILVER":
                a = silver
                b = "\t(SILVER)"
            if ticket == "3": #or ticket.upper == "BRONZE":
                a = bronze
                b = "\t(BRONZE)"
            print "\nThe ticket cost is $"+str(a)+"\n"
            time.sleep(1)
            cost.append(a)
            tick.append(b)
                
print "\n"*40
print "Your final receipt:\n"
print"_"*40
print "|               RECEIPT"
print "|"
for x in range(0,len(cost)):
    print "| Ticket "+str(x+1)+": $"+str(cost[x])+"0"+str(tick[x])
    money+= cost[x]
print "|\n|\n|               SUBTOTAL\n|\t$"+str(money)+"0"
print "|\n|                TOTAL\n|\n|\t$"+str(money)+" x 1.13 = $"+str(money*1.13)
print "_"*40
print "\n\nHave a good day!"

    
                