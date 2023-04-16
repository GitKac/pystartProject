n = int(input('Please enter number: '))

if n % 5 == 0 or n % 11 == 0:
    # maths rest from  div 5
    if n % 5 == 0:
        print(f'Number {n} is divided by 5')
    # maths rest from  div 11
    elif n % 11 == 0:
        print(f'Number {n} is divided by 11')
# maths rest from  div 5 and 11
if n % 5 == 0 and n % 11 == 0:
    print(f'Number {n} is divided by 5 and 11')
else:
    print(f'Number {n} is NOT divided by 5 or/and 11')
