# lists_example_003_app_ext_diff.py
#
append: Appends object at the end.

x1 = [1, 2, 3]
x1.append([4, 5])

x2 = [1, 2, 3]
x2.extend([4, 5])
print ("x1 modified using append [4,5]", x1)
print ("x2 modified using extend [4,5]", x2)
