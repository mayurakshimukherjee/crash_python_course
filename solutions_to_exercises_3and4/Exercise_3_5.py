
    
"""General idea : We have the list of prime numbers, we run through it to see which one of them can factorise
the number. If a set of numbers  can, then those numbers are the prime factor of the number 
"""
from my_package import module_ccp
from my_package.module_ccp import primenumber


def primefactors(i):
    PF =[] # list to store all the prime factors
    PM = primenumber(i) # Calling the primenumber function which I defined before to return all the prime numbers until the entered number
    for pn in range(len(PM)):
        if i%PM[pn]==0: # To see what prime numbers (below the entered number) can divide the  number entered
            PF.append(PM[pn])
        else:
            continue
    return(PF)        

def test_1(k): 
    """ Scan test : This test scans all the numbers until the number whose prime factors are to be found, and saves the numbers          which can divide the number in context and is itself a prime number.
    """
    A=[]
    for i in range(2,k+1):
        if k%i!=0:
            flag =1
        else:
            A.append(i) # A has all the numbers that can divide the number k
            for l in range(len(A)):
                if i%A[l]==0 and i!=A[l]:
                    A.pop(len(A)-1) # After popping off A has only the numbers which can divide itself and no other numbers. 
                    break
    print("Test generated primefactors are: ",A)  
    if A==primefactors(k):
        return"Scan test reveals that the function  'primefactors' work  "
    else:
        return"Scan test reveals that the function  'primefactors' does not work"





if __name__ == '__main__' :
    num = int(input("Please enter a positive integer whose prime factors you want to find out  : "))
    print("The entered number is:", num)
    print("The list of prime numbers until the input number  are :", primenumber(num))
    print("The prime factors of the given number is :", primefactors(num))
    print("Scan test:  ",test_1(num))
    
