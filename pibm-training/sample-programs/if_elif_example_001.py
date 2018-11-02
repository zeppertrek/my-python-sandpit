#if_elif_example_001.py

monthNum = int(input('Please enter the month (1 to 12)'))

#Use of if elif avoids nesting 
# try re-writing this program to use just if else 
if monthNum == 1:
    print ("Jan-", monthNum)
elif monthNum == 2:
    print ("Feb-", monthNum)
elif monthNum == 3:
    print ("Mar-", monthNum)
elif monthNum == 4:
    print ("Apr-", monthNum)
elif monthNum == 5:
    print ("May-", monthNum)
elif monthNum == 6:
    print ("Jun-", monthNum)
elif monthNum == 7:
    print ("Jul-", monthNum)
elif monthNum == 8:
    print ("Aug-", monthNum)
elif monthNum == 9:
    print ("Sep-", monthNum)
elif monthNum == 10:
    print ("Oct-", monthNum)
elif monthNum == 11:
    print ("Nov-", monthNum)
elif monthNum == 12:
    print ("Dec-", monthNum)
else:
    print ("Wrong number, was it really that difficult, try again - ", monthNum)
