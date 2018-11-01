#exception-1.py

# with something_that_returns_a_context_manager() as my_resource:
#    do_something(my_resource)
#    ...
#    print('done using my_resource')
#

try: 
    with open('zzz_random.zzz', 'r') as infile:
        for line in infile:
            print('> {}'.format(line))

except IsADirectoryError:
    print ("zzz_random.zzz is a directory")
except FileNotFoundError:
    print ("my_orders_list.txt does not exist")
#catch all exception handler
except:
    print ("some unknown error occurred")