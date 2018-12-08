#for_loop_example_001.py

# List of first 10 odd numbers
numbers = [1,3,5,7,9,11,13,15,17,19]

# variable to store the sum
oddsum = 0

# iterate over the list
# Note - There is no indexing involved
for val in numbers:
    oddsum += val

# Output: 
print("The sum calculated the for loop without indexing is", oddsum)

# Program to iterate through a list using indexing

# iterate over the list using index
oddsum = 0
for i in range(len(numbers)):
    print (numbers[i], "odd sum value - ", oddsum )
    oddsum += numbers[i]

# Output: 
print("The sum calculated the for loop WITH indexing is", oddsum)