x0 = 1.76 # проміжок
xk = -2.5 # проміжок
dx = -0.25 # крок
b = 35.4
x = x0

while x >= -2.5 and x <= 1.76:
    if x >= -2.5:
        x = x + dx

    y = (10**-3) * (x**5/2) + x + b

    print(y)


print("кінець програми")
