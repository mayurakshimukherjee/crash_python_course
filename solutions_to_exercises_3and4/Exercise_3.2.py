 

def fibonacci(n): 
    """The fibonacci function prints the fibonacci series upto the term number specified. Note here n starts 
    from 0 so here the 10th term would show the series containing 11 terms  
    """
    i=0
    f_list=[0,1]
    k=1
    for i in range(n-2):
        j = f_list[i]+f_list[i+1]
        f_list.append(j)
    return(f_list)

def only_evens(L): 
    """It takes a list and makes a shorter list with only the even indices.
    """
    E=[]
    for i in range(len(L)):
        if i%2==0:
            E.append(L[i])
    return(E)
def only_odds(K): 
    """It takes a list and makes a shorter list with only the even indices.
    """
    O=[]
    for i in range(len(K)):
        if i%2!=0:
            O.append(K[i])
    return(O)            

def test_1(M):
    """ Sequence Test : In Test-1 we check whether the sum of the ith element and (i+1)th element for all i is equal to the (i+2)th element of the Fibonacci series
    """
    i=0
    while(i<(len(M)-2)):
        if M[i]+M[i+1] ==M[i+2]:
            i+=1
    print(i,len(M))
    if i == len(M)-2:
        return 'Test declares the above  list is a Fibonacci series '
    else:
        return 'Test declares the above  list is not a Fibonacci series '

    
def test_2(E,O):
    """ Odd Even Test: In Test_2 we use the rule that the nth number of the even list must be the result of sum of first n numbers on the odd list"""
    i=1
    while(i<(len(E))):
        k=E[i]
        j=0
        a=0
        b=0
        while(j <(i)):
            a = b+O[j]
            b=a
            j+=1
        if a == k:
            flag =1
        else:
            flag =2
            break
        i+=1
            
    if flag !=2:
        return 'Test declares the above  list is a Fibonacci series '
    else:
        return 'Test declares the above  list is not a Fibonacci series '
            
        

if __name__ == '__main__' :
    num = int(input("Please enter an integer to identify the number of terms : "))
    print("The entered number is:", num)
    print(f'Fibonacci series until the {num}th term is',fibonacci(num))
    print(f'Test_1: Sequence Test Result:',test_1(fibonacci(num)))
    print("Only even terms in Fibonacci series",only_evens(fibonacci(num)))
    print("Only odd terms in Fibonacci series",only_odds(fibonacci(num)))
    print(f'Test_2: Odd Even Test Result:',test_2(only_evens(fibonacci(num)),only_odds(fibonacci(num))))
    
          
          