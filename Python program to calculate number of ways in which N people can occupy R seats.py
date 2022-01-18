import math
N=int(input ("Enter the number of students : "))
R=int(input("Enter the number of seats"))
nume=math.factorial(N)
deno=math.factorial(N-R)

no_of_ways = nume//deno

print("Total number of ways are : " + str(no_of_ways))
