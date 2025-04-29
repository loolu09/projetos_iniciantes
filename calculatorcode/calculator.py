
import math

input('==================\nArea Calculator 📐\n==================\n1) Triangle\n2) Rectangle\n3) Square\n4) Circle\n5) Quit')

shape = int(input('Choose a shape to calculate: '))

if shape == 1:
    height = int(input('Enter the value of the height: '))
    base = int(input('Enter the value of the base:'))
    area = (height * base)/2
    print(f'Height:{height}\nBase:{base}\nThe area is {area}')
elif shape == 2:
    length = int(input('Enter the value of the length: '))
    width = int(input('Enter the value of the width: '))
    area = length * width
    print(f'Length:{length}\nWidth:{width}\nThe area is {area}')
elif shape == 3:
    side = int(input('Enter the value of the side: '))
    area = side ** 2
    print(f'Side:{side}\nThe area is {area}')
elif shape == 4:
    radius = int(input('Enter the value of the radius: '))
    area = math.pi * (radius ** 2)
    print(f'Radius:{radius}\nThe area is {area}')
else: 
    print('Quit')