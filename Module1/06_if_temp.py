temperature = float(input('Please put actual temperature in Celsius: '))

if temperature <= 10:
    print('Stay at home')
elif 10 < temperature <= 20:
    print('Take a jacket')
else:
    print('Have a nice day')

print('Stay safe')
