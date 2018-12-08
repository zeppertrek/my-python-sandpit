#if_else_example_001.py

price = int(input('What is the price of the bike? '))
if price > 50000:
    print('The price of the bike - ', price,' is too much, let us use public transport instead')
else:
    print('The price of the bike - ', price,' is in our budget, but lets use public transport instead')
print('Start cycling ')