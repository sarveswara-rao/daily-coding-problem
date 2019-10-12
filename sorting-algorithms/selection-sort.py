# example list to sort
a = [3, 5, 4, 2, 9, 1]
# method 1
print(f'Before sort: {a}')
for i in range(len(a)):
    for j in range(i+1, len(a)):
        m = i
        if a[m] > a[j]:
            a[m], a[j] = a[j], a[m]
print(f'After sort: {a}')


# method 2
for i in range(len(a)):
    m = i
    for j in range(i+1, len(a)):
        if a[m] > a[j]:
            m = j
    if i!=m:
        a[m], a[i] = a[i], a[m]

print(f'After sort: {a}')
