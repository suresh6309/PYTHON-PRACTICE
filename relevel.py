a=input("1.particular month  2.year and month")
import calendar
if a=="1":
    year=int(input("enter year:"))
    month=int(input("enter month:"))
    print(calendar.month(year,month))
elif a=="2":
    year=int(input("enter year"))
    print(calendar.calendar(year))
else:
    print("enter correct option")
