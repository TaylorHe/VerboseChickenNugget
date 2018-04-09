s = []
try:
	print s[0]
except Exception as e:
	raise IndexError(e)