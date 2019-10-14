# func_with_decorators_varying_args_02.py
#
#
# WIP 
# Goal - Undetermined number of arguments for the decorator as well as the functions to be decorated 
# 
# The code below is quite mysterious. Explore 
#


from functools import wraps, partial
import time

def sleep(func=None, *, seconds=None, msg=None):
    if func is None:
        return partial(sleep, seconds=seconds, msg=msg)

    seconds = seconds if seconds else 1
    msg = msg if msg else 'Sleeping for {} seconds'.format(seconds)

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(msg)
        time.sleep(seconds)
        return func(*args, **kwargs)
    return wrapper


# Parameters when passed must be named 
def logarythmic(func=None, *, loglevel=None, logmsg=None):
    if func is None:
        return partial(logarythmic, loglevel=loglevel, logmsg=logmsg)

    loglevel = loglevel if loglevel else -99
    logmsg = logmsg if logmsg else 'Logmessage is not available' 

    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Log Level and Log Message", loglevel, logmsg)
        return func(*args, **kwargs)
    return wrapper




	
	
if __name__ == '__main__':

    def call_n_times(func, n=3):
        # Use of "_" - means that one does not need to use the iterator value 
        for _ in range(n):
            func()

    @sleep  # works now!
    def hello():
        print('hello world')

    print('\nWithout args\n---')
    call_n_times(hello)


    @sleep(seconds=2)
    def hello():
        print('hello world')

    print('\nWith one opt arg: seconds\n---')
    call_n_times(hello)


    @sleep(seconds=1, msg='I work so hard, resting a bit')
    def hello():
        print('hello world')

    print('\nWith two opt args: seconds and msg\n---')
    call_n_times(hello)
	
	
    @logarythmic
    def hello():
        print ("Hello cruel world")
    hello()

    @logarythmic ( loglevel=202020, logmsg='This is a really bizarre log message')
    def hello():
        print ("Hello cruel world")
    hello()


    @logarythmic (logmsg='This is a really bizarre log message')
    def hello():
        print ("Hello cruel world")
    hello()
