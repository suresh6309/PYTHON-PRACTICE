a=input("enter")
inte=[]
stre=[]
for i in a:
    try:
        int(i)=="int"
        inte.append(i)
    except:
        stre.append(i)
print("integers=",inte)
print("strings=",stre)
