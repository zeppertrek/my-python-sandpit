# py_everything_is_an_obj_003.py
a = [1, 2, 3]
b = a
print(b is a)
print (a)
print (b)

b = a + [1]
print (a)
print (b)

print(b is a)