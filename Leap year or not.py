# 1.2 Write a program that determines whether a year entered by the user is a leap year 
or not using ifelif-else statements.

year = 2020

# To get year (integer input) from the user # #year = int(input("Enter a year: "))

# divided by 100 means century year (ending with 00)

# century year divided by 400 is leap year if (year% 400 == = 0) and (year % 100 == 0): 
print("{0} is a leapyear".format(year))
      
# not divided by 100 means not a century year # year divided by 4 is a leap year elif 
(year % 4 ==0) and (year % 100 != 0) 

print("{0} is a leapyear"
      .format(year))
  #year is not leap year
print("{0} is not a leap year".format(year))