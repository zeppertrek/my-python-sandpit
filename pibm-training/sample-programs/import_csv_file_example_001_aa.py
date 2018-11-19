#import_csv_file_example_001_aa.py

# Using a module from Python's standard library
# Makes it very easy for a user to process .csv files 
import csv

file_name = "sample-programs\quebec-sales-data.csv" 
line_count = 0
#
# The line below automatically opens a file and closes it at 
# the end 
#
car_sales_dict = {}
with open(file_name) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    #
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(row)
            myyearmonth=  row[0].split("-")
            print ("extracted year:", myyearmonth[0], " extracted mth", myyearmonth[1])
            myyr = myyearmonth[0]
            mymth = myyearmonth[1]
            myTempVal = car_sales_dict.get(myyr)
 			# What on earth is None ? 
            # The sole value of the type NoneType. 
            # None is frequently used to represent the absence of a value
            if (myTempVal == None):
                #
                car_sales_dict[myyr] = {mymth : row[1]}				
            else:
                mytempmthkey = myTempVal.get(mymth)
                if (mytempmthkey == None):
                    #
                    car_sales_dict[myyr][mymth] = row[1]	
				    
    print(f'Processed {line_count} lines.')
print (car_sales_dict)	 

print ("----------------------------------")
for x in car_sales_dict:
    print (x, car_sales_dict[x]) 
	