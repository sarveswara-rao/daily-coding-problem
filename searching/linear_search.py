a = [1, 12, 2, 3, 13, 4, 14, 0, 9, 8, 7, 56]

print(f"Given Array: {a}")
n = int(input('Enter the element to search: '))

flag = False
for e in a:
    if e == n:
        flag = True
        break

if flag:
    print('Element is found')
else:
    print('Element is not found')
