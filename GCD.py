num1=int(input ("Enter the first number: "))
num2=int(input ("Enter the second number: "))

def gcdFunction(num1,num2):
    if num1>num2 :
        smaller=num2
    else:
        smaller =num1

    for i in range(1,smaller+1):
        if (num1%i==0)and(num2%i==0):
            gcd=i

    print("The GCD of the two number  : {} ".format(gcd))

gcdFunction(num1,num2)
