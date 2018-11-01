#ctxt-mgr-simple-1.py

# with something_that_returns_a_context_manager() as my_resource:
#    do_something(my_resource)
#    ...
#    print('done using my_resource')
#


with open('what_are_context_managers.txt', 'r') as infile:
    for line in infile:
        print('> {}'.format(line))