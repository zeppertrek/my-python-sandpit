# class_as_a_decorator_001.py 
import functools

# State can be maintained when using a class as a decorator 
class CountCalls:
    # __init__ needs to take func  as an input parameter 
    def __init__(self, func):
        # One needs to use the functools.update_wrapper() function instead of @functools.wraps for stand alone functions 
        functools.update_wrapper(self, func)
        self.func = func
        self.num_calls = 0
    
	# Use of __call__ 
    # This makes the class callable, so that it can stand in for the decorated function.
    # __call__() method is executed each time you try to call an instance of the class
    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"Call {self.num_calls} of {self.func.__name__!r}")
        return self.func(*args, **kwargs)

@CountCalls
def say_whee():
    print("Whee!")

say_whee()

say_whee()