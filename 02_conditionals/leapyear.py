
year = 1600

if (year % 4 == 0 and year % 100 != 0 ):
    print("leap Year")
elif(year % 100 == 0 and year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")