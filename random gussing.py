import random
a=random.randint(1,9)

c=5
for i in range(5):
    
    i=int(input("enter your guss! :"))
    if a==i:
        print('your guss is correct')
        print("congragulation's you scored :{}".format(c*10))
        break
    elif i<a:
        print("your guss is low")
        print("you have only{}".format(c-1))
    elif i>a:
        print("your guss is high")
        print("you have only{}".format(c-1))
    else:
        print("enter the correct")
    c=c-1
    if c==0:
        print("sorry your choices is completed")
        print("the correct number is:{}".format(a))
        print("you scored:{}".format(c*10))
        break
