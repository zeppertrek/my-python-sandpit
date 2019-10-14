# __main__.py 
# The file __main__.py is called when you run your project with the -m module flag

from pyfiler import app 

if __name__ == '__main__':
    print ("Start of __main__ routine")
    app.run()