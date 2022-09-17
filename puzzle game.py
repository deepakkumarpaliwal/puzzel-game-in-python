print("                         WELCOME TO PUZZLE GAME")

print()

import random

list1 = [0,1,2,3,4,5,6,7,8,9]

list2 = []

while len(list2) != 5 :     # unique and random numbers

    x = random.randint(0,9)
    
    if list2.count(x) == 0 :
    
        list2.append(x)
        

list3 = ["UNIFORM","FOOTBALL","FATHER","BREAK","GREEN","AIROPLANE","TABLE","PERFECT","BRILLIANT","SUPPORT","SYSTEM"]

list4 = ["UFNORIM","BFAOLOTL","FHAETR","EBARK","EGERN","LAIARNOPE","BTLAE","FPECETR","IBARNILTL","PSOURPT","TSEYMS"]


j=0

for e in list2 :

    print("Arrange the letters to from a valid word :-\n")
    
    print(list4[e])
    
    string = input()
    
    if string.upper() == list3[e] :
        
        j+=1
        
        print("Correct")
    
    else:
       
         print("Wrong")
        
print("Your Score is :- ",j)
