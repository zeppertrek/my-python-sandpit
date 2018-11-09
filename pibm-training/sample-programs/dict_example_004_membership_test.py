# dict_example_004_membership_test.py
# membership test is for keys only, not for values.

codexy = {"A001": 1234, "B001": 1000000, "C002": 4789,  "F002": 2000}

# Output: True
print("A001" in codexy)

# Output: True
print(222222 not in codexy)

# membership tests for key only not value
# Output: False
print("AA001" in codexy)