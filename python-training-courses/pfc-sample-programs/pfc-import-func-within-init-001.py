# pfc-import-func-within-init-001.py

# This program is running from the root
# pfc-trg-package  is a package that has functions defined in __init__.py 

# Read more to understand why this import works !. create_app is inside __init__.py 
# If you do an import from a package like the one below, it will, by, default, look into __init__.py 
# My guess if it does not find it, at the end it will look into __init__.py 
from pfctrgpackage import trgfunc1, trgfunc2


trgfunc1()

trgfunc2()