#dict_example_003_comprehension.py
# Comprehension is also present for dictionaries 


squares = {x: x*x for x in range(6)}

# Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print(squares)

odd_squares = {x: x*x for x in range(11) if x%2 == 1}

# Output: {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
print(odd_squares)