#if_elif_nesting_example_001.py

myPrice = 100
if myPrice < 200:
    print ("Price is less than 200")
    if myPrice == 150:
        print ("It is 150 which is in range and earns us a profit")
    elif myPrice == 100:
         print ("It is 100... we just break even")
    elif myPrice == 50:
         print ("It is 50 too too low ")
    elif myPrice < 50:
         print ("It is less than 50 too low")
else:
    print ("It is 150 which is in range and earns us a profit")
 
print ("Get the price right ")