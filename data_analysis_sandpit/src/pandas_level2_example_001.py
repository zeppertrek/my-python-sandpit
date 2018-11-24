#pandas_level2_example_001.py 


# Load the Pandas libraries with alias 'pd' 
import pandas as pd 

raw_data = {'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy', 'John'], 
        'last_name': ['Miller', 'Jacobson', ".", 'Milner', 'Cooze', 'Mcnulty'], 
        'age': [42, 52, 36, 24, 73, 45], 
        'preTestScore': [4, 24, 31, 0, 0, 67],
        'postTestScore': [155, 94, 57, 62, 70, 45],
		'IQLevel': [100, 150, 60, 230, 40, None],
		'GPA': [None, 1.65, 2.12, 3, None, 0.56],
		}
raw_data['first_name'] = raw_data['first_name'] + ['Peter', 'Akshay'] 
raw_data['last_name'] = raw_data['last_name'] + ['ng', 'kumar'] 
raw_data['age'] = raw_data['age'] + [None, 33] 
raw_data['preTestScore'] = raw_data['preTestScore'] + [3, 23] 
raw_data['postTestScore'] = raw_data['postTestScore'] + [99, 101] 
raw_data['IQLevel'] = raw_data['IQLevel'] + [22, 300] 
raw_data['GPA'] = raw_data['GPA'] + [0, 5.5] 

raw_data['first_name'] = raw_data['first_name'] + [None] 
raw_data['last_name'] = raw_data['last_name'] + ['Kapoor'] 
raw_data['age'] = raw_data['age'] + [17] 
raw_data['preTestScore'] = raw_data['preTestScore'] + [7] 
raw_data['postTestScore'] = raw_data['postTestScore'] + [91] 
raw_data['IQLevel'] = raw_data['IQLevel'] + [22] 
raw_data['GPA'] = raw_data['GPA'] + [3.3] 

#####################################################################

df = pd.DataFrame(raw_data)
print (df)


print (df.describe())
print()
print (df.info())
#
print()
print ("df.index")
print (df.index)

# 
print (df.head(2))
print()
print (df.tail(3))
print("---df[df[GPA]>3----")
print (df[df['GPA']>3])
print (df[df.GPA>3])

print()

df_filtered1 = df[(df.preTestScore >= 50) & (df.postTestScore < 80)]
print (df_filtered1)

#Viewing specific columns
print() 
print (df['first_name'])

print (df.columns)

print ()

print ("Mean of Posttestscore")

print (df.postTestScore.mean()) 

