a = [1, 2, 6, 7, 12, 15, 19, 40, 90, 100, 123]

# Binary search Iterative Version

print(f"Given Array: {a}")
n = int(input('Enter the element to search: '))

flag = False
# lower, higher, and middle index
l = 0
h = len(a) - 1
m = (l+h)//2

while l < h:
    if a[m] == n:
        flag = True
        break
    elif n > a[m]:
        l = m + 1
    else:
        h = m - 1
    m = (l+h)//2

if flag:
    print(f'{n} is present in the give list')
else:
    print(f'{n} is not present in the given list')
