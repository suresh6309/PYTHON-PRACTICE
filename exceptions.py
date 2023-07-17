try:
    a=int(input("enter the value:"))
    b=int(input("enter the next value:"))
    c=a/b
except NameError:
    print(" this name error")
except ZeroDivisionError:
    print("there is an zero division error")
except TypeError:
    print("this is type error")
except Exception:
    print("some error as occured")
else:
    print("value of c is{}".format(c))
finally print("executed")