# Money Calc
import math


print('Enter PayCheck Amount')
paycheck = int(input())

print('Enter Investment amount')
investment=int(input())

print('Enter crypto amount')
crypto=int(input())

print('Enter savings amount')
savings=int(input())


print('Enter Parking per day')
parking=int(input())
print('How many days a week do you pay for parking?')
parkingdays=int(input())

parkingtotal=parking * parkingdays



#perday $

perday = (paycheck - (crypto + investment + parkingtotal + savings)) / 14



print("You can spend up to $",perday,"a day, and not go broke")