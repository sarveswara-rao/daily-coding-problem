"""Given a start word, an end word, and a dictionary of valid words, 
find the shortest transformation sequence from start to end such that only
 one letter is changed at each step of the sequence, and each transformed word 
 exists in the dictionary. If there is no possible transformation, return null.
  Each word in the dictionary have the same length as start and end and is lowercase.

For example, given start = "dog", end = "cat", and 
dictionary = {"dot", "dop", "dat", "cat"}, return ["dog", "dot", "dat", "cat"].

Given start = "dog", end = "cat", and dictionary = {"dot", "tod", "dat", "dar"}, 
return null as there is no possible transformation from dog to cat."""

d = {'dot', 'dop', 'dat', 'cat'}
print(f'\n{d}\n')
start = input('Enter start: ')
end = input('Enter End: ')
new_word = list(start)
flag = True
lst = [start]
for i in range(len(start)):
	if start == end:
		break
	c = list(end)[-(i+1)]
	new_word[-(i+1)] = c
	if "".join(new_word) in d:
		lst.append(''.join(new_word))
		continue
	else:
		flag = False
		break
if flag:
	print(f"\n{lst}")
else:
	print('Unable to transform')