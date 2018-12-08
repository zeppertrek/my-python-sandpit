#dictionary_with_zip.py	

names = ['Year1', 'Year2', 'Year3', 'Year4']
numbers = [2008, 2009, 2010, 2011]
// USe of zip() from the standard library 
d = dict(zip(names, numbers))
print (d)