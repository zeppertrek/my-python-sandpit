#numpy_basics_example_009.py
import numpy as np
import math 
#create a 3x3 array with mean 0 and standard deviation 1 
# in a given dimension

# inline function to print series of n elements 
def calculate_series( n, d): 
  
    # if standard deviation is 0 then print all 
    # elements as 0. 
    if d == 0: 
      
        # print n 0's 
        for i in range(n): 
            print("0", end = ' ') 
        return 1
          
    # if S.D. is even 
    if n % 2 == 0: 
      
        # print -SD, +SD, -SD, +SD 
        i = 1
        while i <= n: 
            print("%.5f"%((math.pow(-1, i) * d)), 
                  end =' ') 
            i += 1
    else: 
        # if odd 
        # convert n to a float integer 
        m = n 
        r = (m / (m - 1)) 
        g = (float)(d * float(math.sqrt(r))) 
          
        # print one element to be 0 
        print("0 ", end = ' ') 
          
        # print (n-1) elements as xi derived 
        # from the formula 
        i = 1
        while i < n: 
            print("%.5f"%(math.pow(-1, i) * g), 
                  end = ' ') 
            i = i + 1
    print("\n") 


ar1 = np.random.normal(0, 1, (3,3))
print (" ********** np array values *************")
print (ar1)

print (" ********** using the inline function *************")
calculate_series (9,1)