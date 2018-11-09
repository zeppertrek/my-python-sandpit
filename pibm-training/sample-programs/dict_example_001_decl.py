#dict_example_001_decl.py

user_roles1 = { 1:"role1, role2", 2:"role1, role2, role3", 3: "role4" }

print ("all about dictionary declarations")
print (user_roles1)


user_roles2 = dict( [ (1, "role1, role2"), (2, "role1, role2, role3"), (3 , "role4") ])

print ("all about dictionary declarations")
print (user_roles2)

# Keys must be simple strings 
user_roles3 = dict( A="role1, role2", B="role1, role2, role3", C= "role4" )

print ("all about dictionary declarations")
print (user_roles3)

