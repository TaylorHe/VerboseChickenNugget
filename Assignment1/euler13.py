#############
# Taylor He, Jacob Manzelmann
# CS370: Project Euler #13 (Modified)
# I pledge my honor that I have abided by the Stevens Honor System.
#		-Taylor He, Jacob Manzelmann
#############

INPUT_FILE = "input13.txt"

class BigInteger():
	''' BigInteger class that handles arithmetic of large numbers '''

	# A list of single-digits integers representing the large integer
	digits = []

	def __init__(self, number_as_string):
		''' Constructor takes in a string as a number '''
		if number_as_string == "" or number_as_string == None:
			print "Error: Empty String or None input."
			raise

		try:
			self.digits = [int(digit) for digit in number_as_string[::-1]] 
		except Exception as e:
			print "Error: {}.".format(e)
			raise

	def to_string(self):
		''' Returns a formatted string representing the BigInteger'''
		while self.digits[-1] == 0 and len(self.digits) > 1:
			self.digits.pop()
		return "".join([str(i) for i in self.digits[::-1]])

	def to_string_10(self):
		''' Returns a formatted string representing the BigInteger'''
		return self.to_string()[:10]

	def get_digits(self):
		''' Returns the digit list '''
		return self.digits

	def __pad_zeroes(self, addend):
		''' Private function used by add() to pad the digits to the 
		larger number. Returns the length of both numbers after padding '''
		addend_len = len(addend.get_digits())
		self_len = len(self.digits)
		if self_len > addend_len:
			addend.digits += ([0] * (self_len-addend_len))
		elif addend_len > self_len:
			self.digits += ([0] * (addend_len-self_len))
		# do nothing if addend_len == self_len
		assert len(self.digits) == len(addend.get_digits())
		return len(self.digits)

	def add(self, addend):
		''' Returns the sum as a BigInteger '''

		# First pad zeroes
		int_len = self.__pad_zeroes(addend)
		
		to_add = addend.get_digits()
		carry = 0
		index = 0
		result_num = ""
		while index < int_len:
			digit_sum = to_add[index] + self.digits[index] + carry
			carry = 1 if digit_sum >= 10 else 0
			result_num += str(digit_sum % 10)
			index += 1

		# If there's a leftover carry, use it
		if carry: result_num += "1"

		# Clean up padding
		while self.digits[-1] == 0 and len(self.digits) > 1:
			self.digits.pop()
		while to_add[-1] == 0 and len(to_add) > 1:
			to_add.pop() 
		
		return BigInteger(result_num[::-1])

		

with open(INPUT_FILE, 'r') as file:
	l = file.read()

if l == "":
	print "Sum is: 0"
	print "First 10 digits: 0"
else:
	a = [BigInteger(n) for n in l.split('\n')]
	res = BigInteger("0")
	for item in a: res = res.add(item) 
	print "Sum is:", res.to_string()
	print "First 10 digits:", res.to_string_10()