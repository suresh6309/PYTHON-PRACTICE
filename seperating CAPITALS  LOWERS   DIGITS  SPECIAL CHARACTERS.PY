a=input("enter:")
u=[]
l=[]
d=[]
s=0
sp=[]
for i in a:
    if i.isupper():
        u.append(i)
    elif i.islower():
        l.append(i)
    elif i.isdigit():
        d.append(i)
    elif i.isspace():
        s+=1
    else:
        sp.append(i)
print("digits:",d)
print("capitals",u)
print("lower case:",l)
print("total space characters:",s)
print("special characters=",sp)
