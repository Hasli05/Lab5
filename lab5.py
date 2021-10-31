arr = [0, 6, 33, 125, 9, 1280, 0, 223]
numeric = arr[0]
number = 0


for numeric in arr:
    if numeric > 0:
        number += 1
    else:
        break


number -= 1
print("Кількість членів послідовності :", number)