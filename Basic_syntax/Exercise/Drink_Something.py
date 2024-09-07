n = int(input())

drink = ''

if n <= 14:
    drink = 'toddy'
elif 14 < n <= 18:
    drink = 'coke'
elif 18 < n <= 21:
    drink = 'beer'
elif n > 21:
    drink ='whisky'

print(f'drink {drink}')