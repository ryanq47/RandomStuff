# Money Calc
import math

print('Enter PayCheck Amount')
paycheck = int(input())

print('Enter Investment amount')
investment=int(input())
print('Enter crypto amount')
crypto=int(input())

#perday $

perday = (paycheck - (crypto + investment)) / 14


print('Your per day spending is:')
print("$",perday)