'''
Created on Apr 11, 2018

@author: Luck
'''
import time

while True:
    choose = raw_input("\nWhich program would you like to try?\n\n1 - Palindrome Checker\n2 - A Knight's Journey\n3 - Persistence\n\n(Press \"0\" and \"ENTER\" to quit!)\n: ")
    
    if choose == "0":
        break
    
    elif choose == "1":
        
        def palindrome(a,c):
            '''palindrome(a,c) - Checks the entered string to see if it's a palindrome or not (spelled same way forwards and backwards)
            a - The user's entered word changed to upper case
            c - The user's original input'''
            
            time.sleep(1)
            b = 0
            
            for x in range (0,len(a)):
                if a[x] == " ":
                    pass
                elif a[x] == a[(x*-1)-1]:
                    b =  "\n\""+c+"\" is a palindrome!"
                else:
                    b = "\n\""+c+" is not a palindrome :/"
                
            return b
                
                
        word = raw_input("\nEnter a word: ")
        word2 = word.upper()
        print palindrome(word2, word)
            
        time.sleep(1)

    elif choose == "2":
        
        letter = ("A","B","C","D","E","F","G","H")
        number = (1,2,3,4,5,6,7,8)
        
        def KnightMove(a,b):
            '''KightMove(a,b) - KnightMove predicts the spaces that the knight can travel to based on its current position on the board
            a - Letter coordinate of user's input
            b - Number coordinate of user's input'''
            
            spots1 = (1,2,-1,-2,1,2,-1,-2)
            spots2 = (2,1,2,1,-2,-1,-2,-1)
            moves = []
            
            for x in range(0,len(letter)):
                if a == letter[x]:
                    a = x
                else:
                    pass
            
            for x in range (0,len(spots1)):
                if a+spots1[x] <= 7 and a+spots1[x] >= 0 and b+spots2[x] <=8 and b+spots2[x] > 0:
                    moves.append(letter[a+spots1[x]])
                    moves.append(b+spots2[x])
                else:
                    moves.append("Not ")
                    moves.append("Possible")
            
            return moves
         
        while True: 
            space = raw_input("\nEnter the space your knight is on (example A1): ").upper()
             
            space1 = space[0]
            space2 = int(space[1]) 
             
            for x in letter:
                if space1 == x:
                    check = 1
                    break
                 
            if space2 <= 0 or space2 > 8 or check == 0:
                time.sleep(1)
                print "\nSorry, but that's not a real space.  Please re-enter your space."   
            else:
                break          
         
        f = KnightMove(space1,space2)
        
        print
        count = 0
        for x in range (0,len(f),2):
            count+=1
            print "Move #"+str(count)+": "+str(f[x])+str(f[x+1])
    
    elif choose == "3":
        
        count = -1
        
        def persistence(a,b):
            '''persistence(a,b) - Calculates the persistence of a number and returns the value of the persistence.
            a - Number user enters
            b - The counter'''
            
            a,num = str(a),1
            b+=1
            
            if len(a) == 1:
                return "\nThe persistence of this number is: "+str(b)
            
            nums = []
            
            for x in range (0,len(a)):
                nums.append(int(a[x]))
                
            for x in range (0,len(nums)):
                num*=nums[x]
            a = num
            
            return persistence(a,b)
            
                
        number = input ("\nEnter a whole number to find it's persistence: ")
        
        if number != int(number) or int(number) < 0:
            print "\n"+str(number)+" is not a whole number.  Please enter whole numbers."
        print persistence(str(number),count)
    
    else:
        pass