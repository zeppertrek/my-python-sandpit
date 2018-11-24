#dict_nested_dict_example_008.py

# This code sample explains how to populate a nested dictionary
# {1:{"Name": "x", "Age":24, "Gender": "F", "Active" : "Y"}, 2:{"Name": "y", "Age":34, "Gender": "M", "Active" : "Y" }}


people_info = {}

# Check if a key value exists
myKeyValue = people_info.get(1)

#If the key does not exists, above function returns "None" 
if myKeyValue == None:
    #people_info[1] = {}
    people_info[1] = {"Name": "maxy", "Age":24, "Gender": "F", "Active" : "Y"}

myKeyValue = people_info.get(2)
   
if myKeyValue == None:
    #people_info[2] = {}
    people_info[2] = {"Name": "flaxy", "Age":34, "Gender": "F", "Active" : "Y"}

print (people_info)

for k,v in people_info.items():
    print (k,v)