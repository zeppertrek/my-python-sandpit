#timeit_lists_vs_dict_example_001.py
import timeit

list1=[]
dict1={}
for i in range(100000):
    list1.append(i)
    dict1[i]=i

print (len(list1))
print (len(dict1))


