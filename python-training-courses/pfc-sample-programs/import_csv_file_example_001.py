#import_csv_file_example_001.py

# Using a module from Python's standard library
# Makes it very easy for a user to process .csv files 
import csv

file_name = "sample-programs\student_academic_record_sample.csv" 
line_count = 0
#
# The line below automatically opens a file and closes it at 
# the end 
#
with open(file_name) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    #
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(row)
            line_count += 1
    print(f'Processed {line_count} lines.')
	
	