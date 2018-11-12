#lists_example_001.py

first_10_odd_numbers = [1,3,5,7,9,11,13,15,17,19]

first_10_even_numbers = [2,4,6,8,10,12,14,16,18,20]

first_20_numbers = first_10_odd_numbers + first_10_even_numbers

print ("Using List comprehension - Single line statement, amazing isn't it  ")
[print(i) for i in first_20_numbers]
