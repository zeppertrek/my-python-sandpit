#for_loop_with_else_clause_001.py
#
#

digits = [0, 1, 4,5,6,7,8,5]
sum = 0

for i in digits:
    print(i)
    sum = sum + i
else:
    print("No items left.")
    print ("The sum of the digits is ", sum )