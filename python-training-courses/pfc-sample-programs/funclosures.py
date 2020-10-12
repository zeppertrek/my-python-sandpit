# funclosures.py
#
# Nested functions
# Closures
#
#

glb_num_1 = 1001
glb_str_1 = "CONTAINERZ1"
glb_list_1 = [101,102,103,104]
#
glb_num_2 = 1002
glb_str_2 = "CONTAINERZ2"
glb_list_2 = [201,202,203,204]
#

glb_num_3 = 9191919191
glb_list_3 = [0,0,0,0,0,0,0,0]
glb_list_303 = [0,0,0,0,0,0,0,303]

def Containerz ():

    nl_num_1 = -100
    nl_str_1 = "non-local-001"
    nl_list_1 = [-4, -3, -2, -1 ]

    # This is our first example of a nested function
    #
    def Box1():
        # Directly accessing global variables inside a nested function. No problem !
        print ("#")
        print ("#Box1()")
        print ("glb_num_1, glb_str_1, glb_list_1 - {} , {},  {}".format (glb_num_1, glb_str_1, glb_list_1))

    def Crate1():
        # Directly accessing non local variables inside a nested function. No problem !
        print ("#")
        print ("#Crate1()")
        print ("nl_num_1, nl_str_1, nl_list_1 - {} , {},  {}".format (nl_num_1, nl_str_1, nl_list_1))

    Box1()
    Crate1()

    def Box2(num_1, str_1, list_1):
        # Passing global values to a nested function from the enclosing function. No problem !
        print ("#")
        print ("#Box2()")
        print ("glb_num_1, glb_str_1, glb_list_1 - {} , {},  {}".format (num_1, str_1, list_1))

    def Crate2(num_2, str_2, list_2):
        # Passing non local values to a nested function from the enclosing function. No problem !
        print ("#")
        print ("#Crate2()")
        print ("nl_num_1, nl_str_1, nl_list_1 - {} , {},  {}".format (num_2, str_2, list_2))

    Box2(glb_num_1, glb_str_1, glb_list_1)
    Crate2(nl_num_1, nl_str_1, nl_list_1)

    def Box3():
        # The global and non local keywords allow for modification
        # of these variables from the enclosing scope inside the inner/nested function
        global glb_num_2
        nonlocal nl_str_1
        nl_list_1 = [5,4,3,2,1,0]
        #
        # This assignment to a global variable should have no effect
        # In this specific case,  Python will create a local variable at run time
        glb_num_1 = 9876
        #
        print ("#")
        print ("#Box3()")
        glb_num_2 = 987654321
        nl_str_1  = "Modified in Box3"
        print ("global glb_num_2, nonlocal nl_str_1, nl_list_1 - {} , {},  {}".format (glb_num_2, nl_str_1, nl_list_1))

    Box3()

    # Passing global mutable and immutable objects to a (nested) function
    # A mutable global list will get modified and the changes persisted beyond
    # the life of the nested function
    def Crate3( immval, mutaval1, mutaval2 ):
        immval = 2020202020
        # Different ways of modifying/resetting a mutable object
        mutaval1 = [3,3,3,3,3,3,3,3,3,3,3,3]
        #
        mutaval2.append(303)
        print ( "Crate3::: immval - {} and mutaval1 - {}".format (immval, mutaval1))

    print("Before Crate3::: glb_num_3 - {} and glb_list_3 - {} and glb_list_303 - {}".format(glb_num_3, glb_list_3, glb_list_303))
    Crate3(glb_num_3, glb_list_3, glb_list_303)
    print("After Crate3::: glb_num_3 - {} and glb_list_3 - {} and glb_list_303 - {} ".format(glb_num_3, glb_list_3, glb_list_303))

print ("#")
print ("#PRE-VALUES - glb_num_1 >> {} .... glb_num_2 >> {} ".format (glb_num_1, glb_num_2)  )
print ("#")
Containerz()
print ("#")
print ("#")
print ("#")
print ("#POST-VALUES - glb_num_1 >> {} .... glb_num_2 >> {} ".format (glb_num_1, glb_num_2)  )

print ("############################################################################################")
print ("##############################End of part 1#################################################")
######################################## PART 2

## Closures
## The nested function must refer to a value defined in the enclosing function.
## The enclosing function must return the nested function.
## The function object (Closure) remembers values in enclosing scopes even if they are not present in memory.

glb_name = "Sanjiv Nagraj"
glb_depts = [ 101, 102, 103, 104, 105, 106]

def  outsider ( strx, stry, strz):
    #
    nl_location = "Mumbai"
    #
    # insider remembers values of variables from the enclosing scope
    #
    def insider():
        insidexy = "--Pune"
        final_str =   strx + stry + nl_location + insidexy
        print ("INSIDER::: final_str - {}".format (final_str))
    return insider

vfunc1 = outsider ( "A", "B", "C")
vfunc1()

def Encirclement( strx, stry, strz):
    #
    nl_location = "Pune"
    #
    # Note - The nested function remembers values from the enclosing scope
    # Python's approach towards handling strz needs to be understood
    #
    def TrappedInside(delta, strz):
        insidexy = "--Wanowarie--"
        final_str = strx + "--" + stry + nl_location + insidexy + glb_name + ":::" + delta + "--" + strz
        print ("TRAPPEDINSIDE::: final_str - {}".format (final_str))
    return TrappedInside

#
vfunc2=Encirclement("1", "2", "3")
vfunc2("cccc", "passedfromabove")

vfunc33=Encirclement("301", "302", "303")
vfunc33("covert", "affairs")

#Traversing through the cell contents to retrieve stored enclosing values
#
for i in vfunc2.__closure__ :
    #print(":::CLOSURE:::" + vfunc2.__closure__[i].cell_contents)
    print (i.cell_contents)

for i in vfunc33.__closure__ :
    #print(":::CLOSURE:::" + vfunc2.__closure__[i].cell_contents)
    print (i.cell_contents)

# Printing values related to the function
print ( "{} -- {} - {} ".format(vfunc33.__name__, vfunc33.__qualname__, vfunc33.__dir__()))


################################################################### PART 3
#############################################################1##### PART 3
###### A closure which accesses a function object from its enclosing scope

print ("######################################## PART3")

def ValuePrinter (x,y):
    print (x,y)

def OuterPerimeter( funcky):
    #
    nl_description = "Inner function references a func from its outer scope"
    #
    # This closure references a function
    #
    def Interior():
        insideinterior = "--Trapped Inside the Outer Perimeter --"
        print (funcky (nl_description, insideinterior ))
    return Interior

#
vnestedfunc = OuterPerimeter (ValuePrinter)
vnestedfunc()

#Traversing through the cell contents to retrieve stored enclosing values
#
for i in vnestedfunc.__closure__ :
    #print(":::CLOSURE:::" + vnestedfunc.__closure__[i].cell_contents)
    print (i.cell_contents)

######################################## PART 4
######################################## PART 4
### Nested function returns a value

print ("######################################## PART4")

# f(x) =  x+y
# f(x) * f(x) = (x+y) (x+y)
# f(x,y)  = x*x + 2* x * y + y*y

def funcxplusy (x,y):
    def quadratic():
        z = x*x + 2*x*y + y*y
        return z
    return quadratic

func1 = funcxplusy(10,20)
y = func1()
print ("funcxy  quad --> func1 - y  ::: {}".format(y))

for i in func1.__closure__ :
    #print(":::func1.CLOSURE:::" + func1.__closure__[i].cell_contents)
    print (i.cell_contents)


######################################## PART 5
######################################## PART 5
### Nested function returns a value

print ("######################################## PART5")

args = [1,2,3,4,5]
kwargs = { "1" : 1, "2" : 2 }

def argsandkwargs (*args, **kwargs):
    #
    def toomanyargsandkwargs():
        argscount = len(args)
        kwargscount = len(kwargs)
        return argscount + kwargscount
    return toomanyargsandkwargs

funckw = argsandkwargs(*args,**kwargs)
y = funckw()
print ("PART 5:::toomanyargsandkwargs  y  ::: {}".format(y))

for i in funckw.__closure__ :
    #print(":::func1.CLOSURE:::" + func1.__closure__[i].cell_contents)
    print (i.cell_contents)




