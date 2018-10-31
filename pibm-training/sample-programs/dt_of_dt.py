#dt_of_dt.py
import pprint

# Start with a new empty dictionary
people = {}

people['Arthur'] = { 'Name': 'Arthur Dent',  'Gender': 'Male',  'Occupation': 'Sandwich-Maker',  'Home Planet': 'Earth' }
people['Trillian'] = { 'Name': 'Tricia McMillan',  'Gender': 'Female',  'Occupation': 'Mathematician',  'Home Planet': 'Earth' }
people['Robot'] = { 'Name': 'Marvin',  'Gender': 'Unknown',  'Occupation': 'Paranoid Android',  'Home Planet': 'Unknown' }

# Another example of using Python's standard library
pprint.pprint(people)