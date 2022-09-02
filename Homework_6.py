'''
Created on Apr 5, 2017

@author: Luqmaan
'''
import time

print "Welcome to the \"Least coins needed\" program"
money = input ("Please input the amount of money you would like to have in coins: ")
money1 = money*100
loon = int(money1)/100
loon1 = int(money1)%100
quart = loon1/25
quart1 = loon1%25
dime = quart1/10
dime1 = quart1%10
nick = dime1/5
nick1 = dime%5

time.sleep(1)
print "You will need: \n"
time.sleep(1)
print "Loonies: "+str(loon)
time.sleep(1)
print "Quarters: "+str(quart)
time.sleep(1)
print "Dimes: "+str(dime)
time.sleep(1)
print "Nickels: "+str(nick)
time.sleep(1)
print "Pennies: "+str(nick1)
