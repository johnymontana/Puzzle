def list_or_tuple(x):
	return isinstance(x, (list, tuple))

def flatten(sequence, to_expand=list_or_tuple):
	for item in sequence:
		if to_expand(item):
			for subitem in flatten(item, to_expand):
				yield subitem
			else:
				yield item


for x in flatten([[1,2,3],[4,5,6],[7,8,9]]):
	print x
