import math

Ax = float(input('Please enter Ax: '))
Ay = float(input('Please enter Ay: '))
A = (Ax, Ay)

Bx = float(input('Please enter Bx: '))
By = float(input('Please enter By: '))
B = (Bx, By)

# Calculating the middle of A&B
a_tr = (Bx - Ax)
b_tr = (By - Ay)
S = (a_tr, b_tr)

print(f'The middle of two points A&B is {S}')

# Calculating distance between A&B
AxBx = ((Ax - Bx) ** 2 + (Ay - By) ** 2)
AB = math.sqrt(AxBx)

# Calculating radius of the circle
r = AB / 2

print(f'The radius of the circle with middle {S} is r= {r}')

# Calculating area of the circle
if r > 0:
    Pi = math.pi
    P = Pi * r ** 2
    print(f'The are of the circle with radius r= {r} is P= {P}')
else:
    print(f'Can not calculating as r ({r}) is less or equal 0')

# Calculating area of a rectangle
c_rect = AB
hc = r
P_rect = (c_rect * hc) / 2
print(f'The area of rectangle is {P_rect}')

# Calculating circumference of a rectangle
sin = math.sin(45)
a_rect = sin * c_rect
print(f'Side a={a_rect}')
b_rect = (2 * P_rect) / a_rect
print(f'Side b={b_rect}')

O_rect = a_rect + b_rect + c_rect
print(f'The circumference of a rectangle is O= {O_rect}')


