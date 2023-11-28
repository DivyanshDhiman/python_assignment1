PENNY_VALUE = 1
NICKEL_VALUE = 5
DIME_VALUE = 10
QUARTER_VALUE = 25
PENNIES_IN_DOLLAR = 100

x=int(input("Write number of pennies: "))
y=int(input("Write number of nickles: "))
z=int(input("Write number of dines: "))
a=int(input("Write number of quarters: "))

totalCent= (x*PENNY_VALUE) + (y*NICKEL_VALUE) + (z*DIME_VALUE) + (a*QUARTER_VALUE)

totalDollars = totalCent/PENNIES_IN_DOLLAR

if totalDollars==1:
    print("Congratulations!The amount you entered was exactly one dollar! You win the game!")

elif totalDollars<1:
    print("Sorry, the amount you entered was less than one dollar")

else:
    print("Sorry, the amount you entered was more than one dollar.")