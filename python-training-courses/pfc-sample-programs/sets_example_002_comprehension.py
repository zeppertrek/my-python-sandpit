#sets_example_002_comprehension.py


mySkills = {skill for skill in ['GIT', 'PYTHON', 'SQL'] if skill not in {'GIT', 'PYTHON', 'JAVA'}}

print (mySkills)