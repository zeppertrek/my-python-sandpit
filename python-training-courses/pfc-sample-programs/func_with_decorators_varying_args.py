# func_with_decorators_varying_args.py
#
#
# WIP 
# Goal - Undetermined number of arguments for the decorator as well as the functions to be decorated 
# 
#
#



glb_list = [1,2,3,4,5,6]
glb_dict = {"1" : "Django", "2" : "Flask" } 
#
func_list = ["a", "b", "c"]
func_dict = {"111111" : "fffffffDjango", "2222222" : "fffffffffFlask" } 

def decorator_function_with_arguments(*deco_args1, **deco_kwargs1):
    def outer_wrap(func_to_be_decorated):
        print("Just Inside outer_wrap()")
        def func_2b_decorated_wrapper(*func_args1, **func_kwargs1):
            print ("func_2b_decorated_wrapper - Voila", func_to_be_decorated.__name__)
        return func_2b_decorated_wrapper
    return outer_wrap

# Here, the decorator has no arguments
@decorator_function_with_arguments()
def sayHello1(a1, a2, a3, a4):
    print('sayHello1 arguments - 4 of them :', a1, a2, a3, a4)

# Here, the decorator has arguments
@decorator_function_with_arguments(1,2,3,4)
def sayHello2():
    print('sayHello2')


# Here, the decorator has args and kwargs
@decorator_function_with_arguments(*glb_list, **glb_dict)
def sayHello3():
    print('sayHello3')

# Here, the decorator has args and kwargs
@decorator_function_with_arguments(*glb_list, **glb_dict)
def sayHello4(*func_list, **func_dict):
    print('sayHello4')

# Here, the decorator has args and kwargs
@decorator_function_with_arguments(*glb_list)
def sayHello5(**func_dict):
    print('sayHello4')

def main():
    sayHello1("a", "aa", "aaa", "aaaa")
    sayHello2()

main()
