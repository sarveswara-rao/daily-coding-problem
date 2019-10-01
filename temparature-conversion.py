# asking the user to enter temp
f1 = input('Enter the temparature in F: ')
# converting from string type to float type
f1 = float(f1)
# now converting it into C
c1 = (5/9)*(f1-32)
print(f'Temp in Celsius: {c1}')

# asking the user to enter temp
c2 = input('Enter the temparature in C: ')
# converting from string type to float type
c2 = float(c2)
# now converting it into C
f2 = (9/5)*c2 + 32
print(f'Temp in F: {f2}')
