user_height = float(input('What is your height in meters: '))
user_weight = float(input('What is your weight in kg: '))

BMI = user_weight / user_height ** 2

print(f'Your BMI score is: {BMI}')
