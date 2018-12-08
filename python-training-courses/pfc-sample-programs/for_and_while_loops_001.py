#for_and_while_loops_001.py

# Prints out 0,1,2,3,4

count = 0
while True:
    print(count)
	# This is the same as count = count + 1 
    count += 1
    if count >= 5:
        break

# Prints out only odd numbers - 1,3,5,7,9
for x in range(10):
    # Check if x is even
	# modulus operator
    if x % 2 == 0:
        continue
    print(x)