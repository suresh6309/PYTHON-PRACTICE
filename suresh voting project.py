# this v1 is containing the data  of the voters id 
vl=eval(input("enter all the voters ids"))
vta=[]
t=0
y=0
c=0
while True
    name=input("enter your name:")
    vt=int(input("enter your voter id:"))
    print("===================================================================")
    print("select your favourite  1.t    2....y   3..c    4...exit ")
    ch=input("enter your favourite ")
    if  ch=="1":
        if vt in vl:
            if vt in vta:
                print("sorry your already used")
                print("=====================================================================================================")
                
            else:
                print("thanks for using the application")
                vta.append(vt)
                t=t+1
                print("=====================================================================================================")
                
        else:
            print("your id is not in the list ")
    elif ch=="2":
         if vt in vl:
            if vt in vta:
                print("sorry your already used")
                print("=====================================================================================================")
                
            else:
                print("thanks for using the application")
                vta.append(vt)
                y=y+1
                print("=====================================================================================================")
        else:
    
            print("your id not in the list")
    elif ch=="3":
         if vt in vl:
            if vt in vta:
                print("sorry your already used")
                print("=====================================================================================================")
                
            else:
                print("thanks for using the application")
                vta.append(vt)
                c=c+1
                print("=====================================================================================================")
         else:
            print("your id is not in the list")
    elif ch=="3":
            
        re=input("1.results   2..exit")
        if re=="1":
            print("enter your id to conform who your are:")
            id=int(input("enter your peronal id:"))
            while(3):# id ==code
                if id==1122:
                    print("welcome to the voting result")
                    print("voting has been completed")
                    print("total votes for t=",t,"total votes for y=",y )
                    if t>y:
                        print("t has won")
                        print("total voters used is ",t+y,"/n used ids are ",vta)
                        break
                    elif y>t:
                        print("y has won")
                        break
                    else:
                        print("this game is draw")
                        break
                else:
                    c=3
                    print("you have only chances of:",c)
                    c=c-1
                    if c==0:
                        print("sorry you are not eligible to show the results")
                        break
                
        else:
            break
        
    else:
        print("enter the correct one")
        
        

        
