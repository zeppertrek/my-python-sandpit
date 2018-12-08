#lists_example_002.py
 
boxers = ['muhammad ali', 'joe frazier', 'sonny liston', 'george foreman']

if 'joe frazier' in boxers:
    print ('Joe Frazier is in the list')
	
 ## append elem at end
boxers.append('sugar ray robinson')

## insert elem at index 0  
boxers.insert(0, 'Mike Tyson') 

## add list of elems at end
boxers.extend(['Joe Louis', 'Thomas Hearns'])  

print (boxers)  
#
print  ("Index of Thomas Hearns is ", boxers.index('Thomas Hearns')    

#
boxers.remove('Thomas Hearns')         
boxers.pop(1)                  
print ( boxers )