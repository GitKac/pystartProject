Ax = float(input('Please enter Ax peak: '))
Ay = float(input('Please enter Ay peak: '))
A = (Ax, Ay)

Bx = float(input('Please enter Bx peak: '))
By = float(input('Please enter By peak: '))
B = (Bx, By)

Cx = float(input('Please enter Cx peak: '))
Cy = float(input('Please enter Cy peak: '))
C = (Cx, Cy)

if A == B == C:
    AB = ((Bx - Ax) ** 2 + (By - Ay) ** 2) ** 0.5
    BC = ((Cx - Bx) ** 2 + (Cy - By) ** 2) ** 0.5
    AC = ((Cx - Ax) ** 2 + (Cy - Ay) ** 2) ** 0.5
    p = (AB + BC + AC) / 2.0
    P_ABC = (p*(p-AB)*(p-BC)*(p-AC))**0.5
    print(f'Area: {P_ABC}')
else:
    print('The peaks of the triangle are not equals')
