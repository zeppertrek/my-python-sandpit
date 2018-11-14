# import_country_states_data_example.py

# country, state
# US, Texas
# US, New York
# US, Alabama
# India, Maharashtra
# India, Karnataka
# India, Kerala

# What we want 
# {US:[Texas, New York, Alabama], India : [Maharashtra, Karnataka, KErala]}

file_name = "sample-programs\country_states_sample_data.csv" 
line_count = 0
#
# The line below automatically opens a file and closes it at 
# the end 
#
import csv 
# initialize empty dictionary 
country_states_dict = dict()
with open(file_name) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    #
    for row in csv_reader:
        #
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
        else:
            #print ("Country and state row values - ", row[0], row[1])
            myStateValues = country_states_dict.get(row[0])
            #print ("Before IF - my state values from dict, current state and line count - ", myStateValues, row[1], line_count)
			
			# What on earth is None ? 
            # The sole value of the type NoneType. 
            # None is frequently used to represent the absence of a value
            if (myStateValues == None):
                # pass
                # country_states_dict[row[0]] = list(row[1])
                # print ("[].append((row[1]))", [].append((row[1])))
                myList = []
                myList.append(row[1])
                print ("myList contents",  myList)
                country_states_dict[row[0]] = myList
            else:
                myList = []
                myList = myStateValues  + [row[1]]
                country_states_dict[row[0]] = myList
        line_count += 1
#
# 
print (country_states_dict)				