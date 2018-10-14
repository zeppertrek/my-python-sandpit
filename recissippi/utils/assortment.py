#
#########################################  
# For later ... Everthing is an object in Python
# and how freaky this can be 
# List with mixed values 
# this is an empty list 
# prices = []
# vowels = ['a', 'e', 'i', 'o', 'u']
# car_details = [ 'Toyota', 'RAV4', 2.2, 60807 ]
# Amazing !!!!!!!!!!!!!!!!!!!!!!!!
# everything = [ prices, vowels, car_details ]
#########################################3

# this is a list with values 
days_of_the_week = [ "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday" ]

months_of_the_year = ["jan", "feb", "mar", "apr", "may",  "jun", "jul", "aug", "sep", "oct", "nov", "dec"]

range_sum = 0

def sum_range_values ( upper_bound):
    for i in range (upper_bound):
        range_sum = range_sum + i
		
    return range_sum
	
	
def return_the_day ( daynum ):
    if (daynum not in (0,1,2,3,4,5,6)):
        daynum = 1
    return days_of_the_week[daynum]
    
def return_the_year (monthnum):
    if (monthnum not in (0,1,2,3,4,5,6,7,8,9,10,11)):
        monthnum = 1
    return months_of_the_year[monthnum]
	
def main():
    print ( return_the_day(1))
    print ( return_the_day(-1))
	
    print ( return_the_year(11))
    print ( return_the_year(13))
	
main()
	
	