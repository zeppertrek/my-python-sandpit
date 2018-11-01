#exception_003.py
#
#
import sys

try:
    # start without the text file
	# then include the text file with strings
    f = open('integers.txt')
    s = f.readline()
    i = int(s.strip())
except IOError as err:
    print ("type of err.args", type (err.args))
    errno, strerror = err.args
    print("I/O error({0}): {1}".format(errno, strerror))
except ValueError:
    print ("No valid integer in line.")
except:
    print ("Unexpected error:", sys.exc_info()[0])
    raise