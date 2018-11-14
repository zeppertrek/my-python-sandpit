# dict_example_006_merging.py
# Python 3.5+ dictionary merging 
# 
user_roles1 = { 1:"role1, role2", 2:"role1, role2, role3", 3: "role4" }
user_roles2 = { 4:"role1, role2", 3:"role1, role2, role3", 8: "role4" }

print ("all about dictionary merging ")
# 
print ("**user_roles1 **user_roles2")
mergedusers1 = { **user_roles1, **user_roles2 }
print (mergedusers1)

print ("**user_roles2 **user_roles1")
mergedusers1 = { **user_roles2, **user_roles1 }
print (mergedusers1)