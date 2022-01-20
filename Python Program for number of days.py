Month = int(input("enter the  month " ))
year = int(input ("enter the year "))

if(Month == 2 and (year%400==0)or ((year%100 !=0) and(year%4 ==0))):
    print("number of days is 29")

elif (Month ==2):
    print("Number of days is 28")
elif(Month ==1 or month == 3 or Month == 5 or Month == 7 or Month ==8 or Month == 10 or Month == 12):
    print("Number of days is 31")
else:
    print("Number of days is 30")
    

