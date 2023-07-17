a=input("enter")
b=input("enter")
i,j=0,0
o=''
while i<len(a) or j<len(b):
    if i<len(a):
        o=o+a[i]
        i=i+1
    if j<len(b):
        o=o+b[j]
        j=j+1
print(o)
    
    
