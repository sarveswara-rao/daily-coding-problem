
"""You are given a list of data entries that represent entries and exits of groups of people into
 a building. An entry looks like this:

{"timestamp": 1526579928, count: 3, "type": "enter"}

This means 3 people entered the building. An exit looks like this:

{"timestamp": 1526580382, count: 2, "type": "exit"}

This means that 2 people exited the building. timestamp is in Unix time.

Find the busiest period in the building, that is, the time with the most people 
in the building. Return it as a pair of (start, end) timestamps.
 You can assume the building always starts off and ends up empty, i.e. with 0 people inside."""

def busiest_period(entries):
	"""
	returns period and max number of people at that period
	"""
	peroid = (None, None)
	num_people, max_num_people = 0, 0

	# sort the entries by timestamp
	sorted_entries = sorted(entries, key=lambda e:e['timestamp'])


	# ro keep track of nunber of people at each entry
	for i, entry in enumerate(sorted_entries):
		if entry['type'] == 'enter':
			num_people += entry['count']
		else:
			num_people -= entry['count']

		if num_people > max_num_people:
			max_num_people = num_people
			period = (entry['timestamp'], sorted_entries[i + 1]['timestamp'])
	return peroid, max_num_people
