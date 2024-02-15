from my_package import module_ccp
from my_package.module_ccp import primenumber
from my_package.module_ccp import primefactors
from my_package.module_ccp import reducer

class Rational() :
    """Documentation of the class:
    
    1. This class will be returning a decimal number as a rational fraction.The decimal number and the 
       level of precision with which it is going to return the fraction, will be the input quantities .
    
    2. Rationaliser fraction (General Overview of the steps) : In the  "A" for loop, I make a list of numbers 
        which will be used to generate the continued fraction. I generate the list again and again until  I have 
        some minimum length of the list, after which I move to the "B" for loop to assemble the numbers in 
        numerators and denominators to see if I   reach the required precision level, If I could not I leave the 
        "B" and go back to continue in the "A" for loop to increase the list size and therefore try and 
        attain higher precision values.  
    """
    
    def __init__( self, numb, precision=1.e-5):
        self.num, self.den = self.rationaliser(numb,precision)
        self.precision = precision
        
    
    
    def rationaliser(self, numb, precision=1.e-5 ):
        """ Case 1 : If the input number can already be represented as an integer with the required  level of 
                     precision, then we do not have to go through the arduous steps of continued fraction """
        if abs(numb - int(numb))<precision:
            sign = 1
            N= int(numb)
            D=1
            flag = 4
            return round(sign*N),round(D)
        
        else:
            """ Case 2 : In other cases, we go forth with continued fractions. """    
            x=abs(numb)
            sign = x/numb
            i=0
            X=[] # The list will take in all the integers of the continued fraction. Integers include integer of  the reciprocal of the differences between the  number and int(number)
            flag=0
            """ Following is the "A" FOR LOOP. Here I have chosen 10 because I dont want to go and over fit the number. 
            In all cases I will reach my required precision level with 6 to 7 steps"""
            for i in range(10): 
                x_int = int(x) # factoring the integer values of x
                diff = abs(x_int - x) # Scooping out the decimal part
                if diff < precision: 
                    X.append(x_int)# Voila we have already reached the number somehow and also completed our list 
                    flag =3
                    """In case, we reach the required precision within 2 steps, we cannot use the generalised 
                       rule I adopted  which requires at least 3 numbers to form a continued fraction. 
                       We can still form a continued fraction this way """
                    if len(X)<3:
                        Y = X[::-1]
                        N =  Y[0]*Y[1]+1
                        D = Y[0]
                        print(N,D)
                        flag =3
                        break
                        
                else:
                    """In cases we dont reach the precision in two steps, we go along with this """
                    y = 1/diff
                    X.append(x_int)
                    x=y 
                if len(X)<2:
                    continue
                Y = X[::-1] # This reverses the list
                Z=[]
                j=0
                """Following is the "B" FOR LOOP"""
                for j in range(len(X)):
                    if j== (len(X)-1): # 
                        break
                    if j == 0:
                        z = Y[j]*Y[j+1] + 1
                        Z.append(z)
                    else:
                        z = Y[j]*Y[j+1] + Y[j-1]
                        Z.append(z)
                    Y[j+1] = Z[j]
                N = Z[j-1] # This is the apparent numerator  as per  continued fraction 
                D = Z[j-2] # This is the apparent denominator as per continued fraction
                frac = N/D
                prec = abs(frac - abs(numb)) 
                """We keep on increasing the list X and there by Z by going back to the "A" for loop unless 
                the numerator and denominator works out in our set level of precision""" 
                if prec < precision:
                    flag=1
                    break
            if flag==1 or 2 or 3 :          
                return reducer(round(sign*N),round(D))
    
    
    
    def __repr__ (self) :
        return f'{type(self).__name__}({self.num}/{self.den})'
    def __str__(self):
        return f'Rational:{self.num}/{self.den}'
    def __eq__(self, other):
        return (self.num,self.den) == (other.num, other.den)
    def __gt__(self, other):
        
        return self.num/self.den > other.num/other.den
    def __lt__(self, other):
        return self.num/self.den < other.num/other.den
    def __add__ (self, other) :
        numb1 = self.num/self.den 
        numb2 = other.num/other.den
        return Rational(numb1 + numb2)
    def __sub__ (self, other) :
        numb1 = self.num/self.den 
        numb2 = other.num/other.den
        return Rational(numb1 - numb2)
    
    def __mul__ (self, other) :
        numb1 = self.num/self.den 
        numb2 = other.num/other.den
        return Rational(numb1 * numb2)
    def __truediv__(self, other) :
        numb1 = self.num/self.den 
        numb2 = other.num/other.den
        if other.num !=0:
            return Rational(numb1 / numb2)
        else:
            return (" Error: Division by 0 ")
        
if __name__ == '__main__' :
    num1 = float(input("Please enter 1st number "))
    num2 = float(input("Please enter 2nd number "))
    p1 = Rational(num1)
    p2 = Rational(num2)
    print("1st number ",p1)
    print("2nd number ",p2)
    print('Addition: ',p1+p2)
    print('Subtraction: ',p1-p2)
    print('Equality: ', p1==p2)
    print('First greater than second? ',p1>p2)
    print('Second greater than first? ',p1<p2)
    print('Multiplication: ',p1*p2)
    print('Divison: ',p1/p2)