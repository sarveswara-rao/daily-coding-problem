
# accept a string from user
s = input('Enter a string: ')
#======================================================#
# Method 1
print('Using Method 1: ', end = ' ')
# to flag when we come across non matching character
flag = 0
# compare from beg.. and from end
for i in range(len(s)//2):
    # if two characters are not equal set the flag
    if s[i] != s[-(i+1)]:
        flag = 1
        # if True then the break from the loop
        break
# check the flag
if flag == 1:
    print(f'"{s}" is not a palindrome')
else:
    print(f'"{s}" is a palindrome')

#======================================================#
# Method two
print('Using Method 2: ', end = ' ')
rev_s = ''.join(list(reversed(s)))

if s == rev_s:
    print(f'"{s}" is a palindrome')
else:
    print(f'"{s}" is not a palindrome')
#======================================================#
