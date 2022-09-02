'''
Created on Apr 3, 2017

@author: Luqmaan
'''
'''
word = raw_input ("Type in your first name: ")
lastn = raw_input ("Type in your last name: ")

print len(word)

print word.upper()
print word.lower()
#print word.relpace('0', '$').
#print word.find ('o') #finds first possible one
#print word.rfind ('o') #finds last possible one
#print word.find ('or') #finds where it starts
print word[0]
print lastn[-1:]
lastn = " Smith"
print word+lastn
word = "John"
print word+lastn

word = word.replace("a" , "$").replace("e" , "$").replace("i" , "$").replace("o" , "$").replace("u" , "$").replace("A" , "$").replace("E" , "$").replace("I" , "$").replace("O" , "$").replace("U" , "$")
print word

a = len(word) - 1
b = len(lastn) - 1

while b >= 0:

    print word[b]
    
    if b == 0:
        
        while a >= 0:

            print word[a]
            
            a = len(lastn) - 1
            
            if a == 0:
                print "done."
            
            else:
                a1 = a - 1
                a = a1
            
    else:
        b1 = b - 1
        b = b1


name = raw_input ("Print your full name here: ")
print name.find(" ")
first = name[0:name.find(" ")]
last = name[name.find(" "):]
a,b = first[0:2], last[0:3]
print b+name[1:-1]+a

'''

first = raw_input ("Print your first name: ")
last = raw_input ("Print your second name: ")
a,b = first[0:2], last[0:2]
c, d = first[2:], last[2:]
print b+c,a+d

