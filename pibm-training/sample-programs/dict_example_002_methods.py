#dict_example_002_methods.py

user_roles1 = { 1:"role1, role2", 2:"role1, role2, role3", 3: "role4" }

# vowels keys
keys = {'a', 'e', 'i', 'o', 'u' }

vowels = dict.fromkeys(keys)
print("generated using fromkeys", vowels)

print ("printing all the items  ", user_roles1.items())

print ("printing all the keys  ", user_roles1.keys())

print ("printing all the values  ", user_roles1.values())

print ("printing the value for 1", user_roles1.get(1))

user_roles1[1] = "rolesXXXX"

user_roles1[4] = "rolesYYYYYY"

print ("printing the value for 1", user_roles1.get(1))
print ("printing the value for 1", user_roles1.get(4))

# delete the element 
# 
user_roles1.pop(4)