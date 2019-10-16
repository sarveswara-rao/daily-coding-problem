"""
Given a linked list, sort it in O(n log n) time and constant space.

For example, the linked list 4 -> 1 -> -3 -> 99 should become -3 -> 1 -> 4 -> 99.
"""

class Node:
	"""Node in a linked list"""
	def __init__(self, val, nxt = None):
		self.val =  val
		self.next = nxt


def sort(head):
	if not head:
		return head

	k=1
	while True:
		first = head
		head = None
		tail = None

		merges = 0
		while first:
			merges += 1
			# move second k steps forword
			second = first
			first_size = 0
			for i in range(k):
				first_size += 1
				second = second.next
				# if we reach end of the list then breakout from the loop
				if second is None:
					break

			# merge list first and second
			second_size = k
			while first_size > 0 or (second_size > 0 and second is not None):
				e = None
				if first_size == 0:
					e = second
					second = second.next
					second_size -= 1
				elif second_size == 0 or second is None:
					e = first
					first = first.next
					first_size -= 1
				elif first.val <= seoncd.val:
					e = first
					first = first.next
					first_size -= 1
				else:
					e = second
					second = second.next
					second_size -= 1

				if tail is not None:
					tail.next = e
				else:
					head = e
				tail = e

			first = second

		tail.next = None

		if merges <= 1:
			return head

		k = k * 2