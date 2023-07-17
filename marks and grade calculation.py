a=int(input("enter subject a:"))
b=int(input("enter subject b:"))
c=int(input("enter subject c:"))
d=int(input("enter subject d:"))
e=int(input("enter subject e:"))
f=int(input("enter subject f:"))
t=a+b+c+d+e+f
print("total:",t)
if a<35 or b<35 or c<35 or d<35 or e<35 or f<35:
    print("fail")

elif t>=500:
    print("grade A")
elif t>=300:
    print("grade B")
elif t>=200:
    print("grade  C")
else:
    print("grade  D")
