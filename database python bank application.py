import mysql.connector
mydb=mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password="123456789",
                database="suresh"
                )

class banking:
    def creating(self):
        mycursor=mydb.cursor()
        a=eval(input("enter"))
        mycursor.execute("select id1 from banking")
        accounts=[]
        for i in mycursor:
            accounts.append(list(i))
        l=len(accounts)
        acc={''}
        for j in range(l):
            acc.add(accounts[j][0])
        if a in acc:
            print("Account already exixts")
        else:
            print("you can create account on this number")

    def created(self):
        mycursor=mydb.cursor()
        id1=input("enter your id")
        name=input("enter your name")
        bal=input("enter balence of first deposited ")
        s="insert into banking values(%s,%s,%s)"
        t=(id1,name,bal)
        mycursor.execute(s,t)
        mydb.commit()

        print ( 'Data entered successfully.' )
    def depositing(self):
        mycursor=mydb.cursor()
        mycursor.execute("select id1 from banking")
        accounts=[]
        for i in mycursor:
            accounts.append(list(i))
        l=len(accounts)
        acc={''}
        for j in range(l):
            acc.add(accounts[j][0])
        no=eval(input("enter account no;"))
        if no in acc:
            data=(no,)
            q="select  bal from banking where id1=%s"
            mycursor.execute(q,data)
            a=[]
            for i in mycursor:
                a.append(list(i))
                b=(a[0][0])
                c=int(input("enter aount to deposit:"))
                d=c+b
                sql = "UPDATE customers SET address = %s  WHERE address = b "
                mycursor.execute(sql)
        else:
            print("please enter correct account number")
  
bank=banking()

while True:
    ch=input("select your choice:\n1:for creating id:\n2:for creating account\n3:for depositing\n4:for crediting\nenter:")
    
    if ch=="1":
            bank.creating()
    elif ch=="2":
        bank.created()
    elif ch=="3":
        bank.depositing()
    else:
        print("enter correct option")
    
