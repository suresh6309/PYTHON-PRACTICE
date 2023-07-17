from time import *
print("***************************************welcome to our website*******************************************")
print("please wait processing is going on")

def balance():
    global a
    id=input("enter your bank id:")
    if id in a:
        print("your balance is:",a[id])
    else:
        print("sorry your account does not exist")
def deposit():
    global a
    global p
    de=input("enter your id:")
    ba=a[de]
    bal=int(ba)
    bala=bal
    print("this requires your password")
    amt=int(input("enter amount:"))
    password=input("enter your password")
    if password==p[de]:
        if bala<amt:
            print("sorry in sufficient balance")
        else:
            print("sussfully the trasation has been completed")
            a[de]=bala-amt
            check=input("enter 1.check balace   2.exit")
            if check=="1":
                print("remaining bal is:",a[de])
            else:
                print("thanks for using")
    else:
        print("please enter correct password")
    
def credit():
    choice=input("1.crediting to another account by you   2. only for bank(official)")
    if choice=="1":
        ac=input("enter your account no:")
        print(b)
        if ac in b:
            global totalamt
            print("your balance is:",a[ac])
            ida=input("enter the domains account number(account number of a person you to transfer:)")
            if ida in b:
                amttra=int(input("enter the ammount"))
                x=a[ida]
                y=int(x)
                totalamt=y+amttra
                a[ida]=totalamt
                aat=a[ac]
                iaant=int(aat)
                atbal=iaant-amttra
                a[ac]=atbal
                print("your balance remaining:",a[ac])
            else:
                print("account not found")
             
        else:
            print("your account not found")
    elif choice=="2":
        bank=int(input("enter the bank code"))
        if bank==1122:
            bta=input("enter the account number:")
            if bta in b:
                btaa=int(input("enter the amount to transfer:"))
                intbta=int(a[bta])
                #converting value into integer and adding amt to the holder
                hab=int(a[bta])
                aath=btaa+hab
                a[bta]=aath
                print("amount of the holder before transfer is:",intbta)
                print("balance after transfer is:",aath)
            else:
                print("account not found")
    else:
        print("select correct choice")
                         
def create():
    
    global a
    global p
    global idsandnames
    
    name=input("enter your name")
    
    cid=input("create your id:")
    idsandnames[cid]=name
    password=input("create your password")
    if cid in a:
        print("sorry this account already exist")
    else:
        a[cid]="100"
        print("hai",name)
        print(" your account has successfully created")
        p[cid]=password

def details():
    global a
    global p
    global idsandnames
    detail=input("enter your id:")
    
    print("hai ",idsandnames[detail],"your balance is:",a[detail] ,"your password is:",p[detail])
def change():
    global p
    global idsandnames
    idaaa=input("enter your account no:")
    print("hai ",idsandnames[idaaa])
    password=input("enter your old password")
    if p[idaaa]==password:
    
        npassword=input("enter your new password:")
        if npassword.isdigit():
            p[idaaa]=npassword
            print("your password has been successfully chaged")
        else:
            print("enter only digit password")
    else:
        print("enter your password correctly")
    

sleep(0)

a={}
b=a.keys()

idsandnames={}
p={}
while True:
    ch=input("select your choice:\n 1:balance enquiry \n 2.withdraw\n 3.deposit\n 4.creating bank account\n 5.details\n 6.change password  \n 7.exit\nenter:")
    if ch=="1":
        balance()
    elif ch=="2":
        deposit()
    elif ch=="3":
        credit()
    elif ch=="4":
        create()
    elif ch=="5":
        details()
    elif ch=="6":
        change()
    elif ch=="7":
        break
    else:
        print("enter correct option")

