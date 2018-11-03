#if_else_ladder_example_001.py 

day_of_the_week = int(input('Please enter the day of the week [ 1 to 7] which starts from Monday'))
if (day_of_the_week == 1):
    print('Day of the week entered as ', day_of_the_week, ' is Monday...bravo')
else:
    if (day_of_the_week == 2):
        print('Day of the week entered as ', day_of_the_week, ' is Tuesday...bravo')
    else:
        if (day_of_the_week == 3):
            print('Day of the week entered as ', day_of_the_week, ' is Wednesday...bravo')
        else:
            if (day_of_the_week == 4):
                print('Day of the week entered as ', day_of_the_week, ' is Thursday...bravo')
            else:
                if (day_of_the_week == 5):
                    print('Day of the week entered as ', day_of_the_week, ' is Friday...you have survived the week ')
                else:
                    if (day_of_the_week == 6):
                        print('Day of the week entered as ', day_of_the_week, ' is Saturday...bravo')
                    else:
                        if (day_of_the_week == 7):
                            print('Day of the week entered as ', day_of_the_week, ' is Sunday...bravo') 	
print('The weekdays go too slow and the weekends too fast')