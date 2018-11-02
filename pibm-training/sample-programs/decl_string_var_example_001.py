# decl_string_var_example_001.py
firstname = "Nice"
lastname  = 'Try' 

full_name =firstname + lastname
print ("full name is ", full_name)

random_str = "<>" * 20

print ("random_str is --", random_str)

i=0
# a string can be treated as a sequence
while i< len(full_name):
    print (full_name[i]) 
    i+=1


txt = '''A string in triple quotes can extend
over multiple lines like this one, and can contain
'single' and "double" quotes.'''

print ("multi line txt is", txt)

txt = "He said: \"It doesn't matter, if you enclose a string in single or double quotes!\""
print("txt is ", txt)