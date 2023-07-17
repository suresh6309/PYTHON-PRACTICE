
from datetime import datetime
time=datetime.now()



def balance():
    global a
    global c
    id=input("enter your bank id:")
    if id in a:
        print("your balance is:",c[id])
    else:
        print("sorry your account does not exist")
def withdraw():
    global l
    global a
    global b
    global c
    global d
    global e
    de=input("enter your id:")
    if de in e:
        print("this requires your password")

        amt=int(input("enter amount:"))
        password=input("enter your password")
        if password==b[de]:
            bal=int(c[de])
            if bal<amt:
                print("sorry in sufficient balance")
            else:
                print("sussfully the trasation has been completed")
                c[de]=bal-amt
                l[de]=time
                check=input("enter 1.check balace   2.exit")
                if check=="1":  
                    print("remaining bal is:",c[de])
                else:
                    print("thanks for using")
        else:
            print("please enter correct password")
    else:

        print("your account not found")
def deposit():
    global l
    global a
    global b
    global c
    global d
    global e
    choice=input("1.crediting to another account by you   2. only for bank(official)")
    if choice=="1":
        ac=input("enter your account no:")
        if ac in e:
            print("your balance is:",c[ac])
            an=input("enter the domains account number(account number of a person you to transfer:)")
            password=input("enter your password")
            if password==b[ac]:
                if an in e:
                    amt=int(input("enter the amount"))
                    c[an]=amt+int(c[ac])
                    g=int(c[ac])-amt
                    c[ac]=g
                    print("transaction successful")
                    print("your balance remaining:",c[ac])
                else:
                    print("account not found")
            else:
                    print("sorry enter correct password")
    
        else:
            
            print("your account not found")
    elif choice=="2":
        bank=int(input("enter the bank code"))
        if bank==1122:
            acc=input("enter the account number:")
            if acc in e:
                i=int(input("enter the amount to transfer:"))
                pa=int(c[acc])
                c[acc]=i+pa
                print("amount of the holder before transfer is:",pa)
                print("balance after transfer is:",c[acc])
                l[acc]=time
            else:
                print("account not found")
    else:
        print("select correct choice")

                         
def create():
    global l
    global a
    global b
    global c
    global d
    global e
    
    name=input("enter your name")
    
    acc=input("create your id:")
    
    password=input("create your password")
    if acc in e:
        print("sorry this account already exist")
    else:
        c[acc]="100"
        print("hai",name)
        print(" your account has successfully created")
        b[acc]=password
        a[acc]=name
        l[acc]=time
    
        

def details():
    global a
    global b
    global c
    global d
    global l
    
    acc=input("enter your account no:")
    password=input("enter your password:")
    if password==b[acc]:

        if acc in e:
            print("hai ",a[acc],"your balance is:",c[acc],"last trasaction is done on",l[acc])
        else:
            print("sorry not found")
    else:
        print("enter correct password ")
    
    
   
def change():
    global l
    global a
    global b
    global c
    global d
    global e
    acc=input("enter your account no:")
    print("hai",a[acc])
    password=input("enter your old password")
    if b[acc]==password:
        npassword=input("enter your new password:")
        b[acc]=npassword
        print("your password has been successfully chaged")
    else:
        print("enter your password correctly")
def total():
    global e
    password=input("ente the password")
    if password=="1122":
        an=len(e)
        print("the no accounts present in these bank",an)
        print("press \n 1: to view accounts  \n 2:to exit")
        c=input("enter:")
        if c=="1":
            print(e)
        elif c=="2":
            print("thanks for using")
        else:
            print("sorry enter correct one")
    else:
        print("you are not the correct person to view the details \n enter the correct password")
l={}# id,last transaction time
a={}#id, name
b={}#id,password
c={}#id, amt
d={}# id, last trans details
e=a.keys()
while True:
    print("***************************************welcome to our website*******************************************")
    print("please wait processing is going on")
    print("===========================================================================================")
    ch=input("select your choice:\n 1:balance enquiry \n 2.withdraw\n 3.deposit\n 4.creating bank account\n 5.more details about transactions \n 6.change password  \n 7.exit\n 8.for more \nenter:")
    print("===========================================================================================")
    if ch=="1":
        balance()
    elif ch=="2":
        withdraw()
    elif ch=="3":
        deposit()
    elif ch=="4":
        create()
    elif ch=="5":
        details()
    elif ch=="6":
        change()
    elif ch=="7":
        print("please enter correct one")
        break
    elif ch=="8":
        print("this is only for the bank purpose \n to know which accounts are present \n to find total number of accounts present")
        total()
        
    else:
        print("enter correct option")


