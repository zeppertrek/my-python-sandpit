#coll_dequeue_example_001.py
# Deque can be implemented in python using the module “collections“.
# Deque is preferred over list in the cases where we need quicker 
# append and pop operations from both the ends of container, as 
# deque provides an O(1) time complexity for append and pop operations 
# as compared to list which provides O(n) time complexity.
#
#O(1) means that it takes a constant time, like 14 nanoseconds, or three minutes 
# no matter the amount of data in the set.
#
# O(n) means it takes an amount of time linear with the size of the set, 
# so a set twice the size will take twice the time. 
# You probably don't want to put a million objects into one of these.
# 
# 



import collections 

strange_words = collections.deque(["alcazar","bezoar","cerulean", "plew"])
print (strange_words) 
print ("*" * 10) 
  
# using append() to insert element at right end  
# inserts 4 at the end of deque 
strange_words.append("piscatorial") 
  
# printing modified deque 
print ("The deque after appending at right is : ") 
print (strange_words) 
  
# using appendleft() to insert element at right end  
# inserts 6 at the beginning of deque 
strange_words.appendleft("dragoman") 
  
# printing modified deque 
print ("The deque after appending at left is : ") 
print (strange_words) 
  
# using pop() to delete element from right end  
# deletes from the right end of deque 
strange_words.pop() 
  
# printing modified deque 
print ("The deque after deleting from right is : ") 
print (strange_words) 
  
# using popleft() to delete element from left end  
# deletes from the left end of deque 
strange_words.popleft() 
  
# printing modified deque 
print ("The deque after deleting from left is : ") 
print (strange_words) 