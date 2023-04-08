import math

sides = float(input('Please enter sides of the equilateral triangle: '))

# Area of equilateral triangle
P_eqTr = (sides ** 2 * math.sqrt(3)) / 4
O_eqTr = 3 * sides

print(f'Area of equilateral triangle is {P_eqTr}')
print(f'Circuit of equilateral triangle is {O_eqTr}')
