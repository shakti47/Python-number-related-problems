num1 = int(input("Enter the first number: "))
num2=int(input("Enter the second number"))
def lcmfinder(num1,num2):
    if num1>num2:
        larger= num1
    else:
        larger=num2
 
    while True:
        if (larger%num1==0)and(larger %num2==0):
            lcm=larger
            break
        larger = larger +1
    print("lcm of the two number : {} ".format(lcm))

lcmfinder(num1,num2)
