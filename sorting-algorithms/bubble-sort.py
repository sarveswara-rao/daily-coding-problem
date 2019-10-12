# example list to sort
a = [3, 5, 4, 2, 9, 1]
# method 1
print(f'Before sort: {a}')

for i in range(len(a)-1):
    for j in range(len(a)-i-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
print(f'After sort: {a}')
