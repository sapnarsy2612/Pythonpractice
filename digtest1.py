year=int(input("enter yr"))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("year ",year,"is a leap year.")
        else:
            print("year ",year,"is not a leap year.")
    else:
        print("year ",year,"is a leap year.")
else:
    print("year ",year,"is not a leap year.")

