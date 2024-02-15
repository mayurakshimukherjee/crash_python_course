
#######################    Exercise 3.1a    #########################

Task: To print numbers divisible by 2, 3, 5, 7 etc

We make use of the divisibility function which takes a variable n and finds whether it is divisible by 2,3,5 or 7 using successive if statements . If it is divisible by 2 it returns a statement that it is dividible by 2 etc and moves to the successive conditional statement. If it is not divisible by any number then it returns "Not divisible by 2, 3, 5 or 7

######################     Exercise 3.1b    #########################

Task: To check whether two input numbers are such that the first is divisible by the other

We make use of the the divisibility_duo function, which  takes two  variables n1 and n2 as inputs  and finds whether the first number is divisible by the second and vice versa and returns a verification statement.

######################     Exercise 3.2      #########################

Task: To define a function to print the fibonacci series upto the nth term

The fibonacci function prints the fibonacci series upto the term number specified. Note here n starts from 0 so here the 10th term would show the series containing 11 terms.

The only_evens function  takes a list and makes a shorter list with only the even indices and likewise for the only_odds. They are used to make the tests for fibonacci function.

Test 1 (Sequence Test) : In Test-1 we check whether the sum of the ith element and (i+1)th element for all i is equal to the (i+2)th element of the Fibonacci series. This serves as the basis of the formation of the Fibonacci series.

Test 2 (Odd Even Test): In Test_2 we use the rule that the nth number of the even list (starting with index 0) must be the result of sum of first n numbers on the odd list. This is a rule that can easily be verified from the even list=[0,1,3,8,21....] and the odd list = [1,2,5,13,34....], where we see 1+2 = 3, and 1+2+5=8 and 1+2+5+13 = 21 and so on.

######################     Exercise 3.4      #########################

Task: To return all prime numbers smaller than 100, starting by knowing that 2 is a prime number

We follow the general idea : We start counters "i", and "j" within the counter "i" . "i" picks a number serially from 2 and 
spans all the number from 2 to 100 ("j") to see if it is divisible by any other number than itself and if it appears that it cannot be divided by any other number then it is stored in a list as a prime number. The details 
are explained in the code.

######################     Exercise 3.5      #########################

Task: To return all the prime factors of an entered positive number.

We follow the general idea : We have the list of prime numbers, we run through it to see which one of them can factorise
the number. If a set of numbers  can, then those numbers are the prime factor of the number.

We do the following test (Scan test) to check if our code works. This test scans all the numbers until the number whose prime factors are to be found, and saves the numbers which can divide the number in context and is itself a prime number without using the prime number function.

######################     Exercise 4      #########################

Task: To prepare a class to define rational numbers

Here are some of the salient features. This class will be returning a decimal number as a rational fraction.The decimal number and the level of precision with which it is going to return the fraction, will be the input quantities .
    
Rationaliser function (General Overview of the steps) : In the  "A" for loop, I make a list of numbers which will be used to generate the continued fraction. I generate the list again and again until  I have some minimum length of the list, after which I move to the "B" for loop to assemble the numbers in numerators and denominators to see if I reach the required precision level. If I could not reach the precision level even after having minimum number of  elements and  moving to the B loop , I leave the "B" and go back to continue in the "A" for loop to increase the list size and therefore try and attain higher precision values. Rest of the documentation is explained with the code.









