#dict_example_007_more_stuff.py


a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})
print (a == b == c == d == e)

d = {"one": 1, "two": 2, "three": 3, "four": 4}

print (list(d))
print (list(d.values()))

a1 = list(d)
a2 = list(d.values())

print ("a1", a1, "and its length is ", len(a1))

print ("a.items()", a.items())


