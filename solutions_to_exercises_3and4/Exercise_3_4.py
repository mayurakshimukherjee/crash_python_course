
""" General idea : We start counters "i", and "j" within the counter "i" . "i" picks a number serially from 2 and 
spans all the number from 2 to 100 ("j") to see if it is divisible by any other number than itself and if it 
appears that it cannot be divided by any other number then it is stored in a list as a prime number. The details 
are explained below 
"""
def primenumber(m):
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
    
if __name__ == '__main__' :
    print('The prime numbers until 100 are: ', primenumber(100))
    
                
            
        