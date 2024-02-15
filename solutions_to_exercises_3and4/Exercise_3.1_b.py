
num1 = int(input("Please enter the first integer: "))
print("The first number is:", num1)
num2 = int(input("Please enter the second integer: "))
print("The second number is:", num2)

def divisibility_duo(n1,n2):
    """The divisibility_duo function takes two  variables n1 and n2 as inputs  and finds whether the first number is divisible by the second  divisible by 2,3,5,7 using successive 
    and vice versa and returns a verification statement
    """
    if n1%n2==0:
        return('The first number is divisible by the second')
    if n2%n1==0:
        return('The second number is divisible by the first')
    else: 
        return('No number is divisible by the other')
print(divisibility_duo(num1,num2))
    