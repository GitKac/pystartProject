before_tax = float(input('Price before tax: '))
VAT = float(input('The VAT: '))

after_tax = before_tax * (1 + VAT / 100)

print(f'The price is {after_tax} including VAT')
