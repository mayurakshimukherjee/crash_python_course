""" General idea : We start counters "i", and "j" within the counter "i" . "i" picks a number serially from 2 and 
spans all the number from 2 to 100 ("j") to see if it is divisible by any other number than itself and if it 
appears that it cannot be divided by any other number then it is stored in a list as a prime number. The details 
are explained below 
"""

def primenumber(m):
    """ This function makes a list of all the prime numbers until the number m starting from 2.
    """
    i=2 # It is already known to us that the first prime number is 2 so we start from 2
    j=2
    PN=[] # List to store the prime number 
    while(i<(m+1)): # first counter to check a prime number 
        ind=0
        j=2
        while(j<(m+1)): # second counter to span through all the numbers for each i to check divisibility
            if i%j==0 and i!=j: # if "i" is divisible by "j" which is a different number than itself 
                ind=1 #then it gives an indication 1 and breaks out of the j loop and resets to try another i for primeness
                break
            j+=1
        
        if ind==0: # this indication ensures that we moved out of the j loop only because we spanned through all the set of numbers and didnt find any divisibility for the respective "i"
            PN.append(i) # We add to the list of prime numbers 
        
        i+=1
    return(PN)


def primefactors(i):
    PF =[] # list to store all the prime factors
    PM = primenumber(i) # Calling the primenumber function which I defined before to return all the prime numbers until the entered number
    for pn in range(len(PM)):
        if i%PM[pn]==0: # To see what prime numbers (below the entered number) can divide the  number entered
            PF.append(PM[pn])
        else:
            continue
    return(PF)        




def reducer(num,den):
    """ This function reduces a fraction denoted as num for numerator and den for denominator 
     into mutually indivisible numbers. So that they do not have any common factors apart from 1""" 
    
    
    """To store the sign of the numerator and work with positive numbers.The sign will be added 
    in the end to reduce complexity."""
    sign = abs(num)/num 
    P = abs(num)
    Q = den
    global P1
    global Q1
    
    """ We make a list of primefactors of P and Q and search through the list to see if they have  
    any common prime factors"""
    
    A = list(primefactors(P))
    B = list(primefactors(Q))
    i=0
    while(i< len(A)):
        j=0
        while(j <len(B)):
            if B[j]==A[i]:
                """Once we find the common prime factors we divide the num and the den by the prime factor
                and make the resultant the new num and den and find their prime factors again and we repeat
                this again and again until we donot have any more common factors. That is when we get out of 
                the loop."""
                global P1
                global Q1
                P1= P/B[j]
                P=P1
                Q1= Q/B[j] 
                Q=Q1
                A = list(primefactors(P1)) 
                B = list(primefactors(Q1))
                i=-1
                break        
            else:
                j+=1    
        i+=1        
    return int(sign*P),int(Q)           