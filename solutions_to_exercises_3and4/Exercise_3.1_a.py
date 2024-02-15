
num = int(input("Please enter an integer: "))
print("The entered number is:", num)


def divisibility(n) :
    """The Divisibility function takes a variable n and finds whether it is divisible by 2,3,5,7 using successive 
    if statements . If it is divisible by 2 it returns a statement that it is dividible by 2 etc and moves to the 
    successive conditional statement. If it is not divisible by any number then it returns "Not divisible by 2, 3, 
    5 or 7"
    """
    if n%2==0:
        print('It is divisible by 2')
    if n%3==0:
        print('It is divisible by 3')
    if n%5==0:
        print('It is divisible by 5')
    if n%7==0:
        print('It is divisible by 7')
    if n%2!=0 and n%3!=0 and n%5!=0 and n%7!=0:
        return('It is divisible by none')
    else:
        return('')    
     
              

print(divisibility(num))

