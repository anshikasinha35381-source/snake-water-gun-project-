import random 
computer = random.choice([-1,0,1])
youstr = input("enter your choice : ")
youDict = {"s":1,"w":-1,"g":0}
reverseDict= {1:"snake",-1:"water",0:"gun"}
you=youDict[youstr]
print(f"you choose {reverseDict[you]}\ncomputer choose {reverseDict[computer]}")
if computer==you:
    print("match is draw")
else:
    if (computer==1 and you==0):
        print("you won")
    elif(computer==1 and you==-1):
        print("you lost")
    elif(computer==0 and you==1):
        print("you won")
    elif(computer==0 and you==-1):
        print("you loose")
    elif(computer==-1 and you==0):
        print("you won")
    elif(computer==-1 and you==1):
        print("you loose")
    else:
        print("something went wrong")
        
        
        
        
        
    
