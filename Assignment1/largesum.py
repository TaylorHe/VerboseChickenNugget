#############
# Taylor He, Jacob Manzelmann
# CS370: Project Euler #13 (Modified)
# January 25, 2018
# I pledge my honor that I have abided by the Stevens Honor System.
#		-Taylor He, Jacob Manzelmann 
#############
import sys

INPUT_FILE = "input.txt"

class BigInteger():
	''' BigInteger class that handles arithmetic of large numbers '''

	# A list of single-digits integers representing the large integer
	digits = []

	def __init__(self, number_as_string):
		''' Constructor takes in a string as a number '''
		if number_as_string == "" or number_as_string == None:
			raise Exception("Error: Empty String or None input.")

		try:
			self.digits = [int(digit) for digit in number_as_string[::-1]] 
		except Exception as e:
			raise Exception("Error: {}.".format(e))

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

		
if __name__ == "__main__":
	# There are two use cases:
	#	python largesum.py defaults to input.txt as the input file
	# 	python largesum.py "input12.txt" takes input12.txt as the input file
	argc = len(sys.argv)
	if argc > 2:
		raise Exception("Usage: python largesum.py [name of file.txt]")

	if argc == 2: INPUT_FILE = sys.argv[1]

	try:
		with open(INPUT_FILE, 'r') as file:
			l = file.read()
	except Exception as e:
		raise Exception(e)


	num_list = []
	for i in l.split('\n'):
		if i != "": num_list += [BigInteger(i)]
	res = BigInteger("0")
	for item in num_list: res = res.add(item) 
	print "Sum is:", res.to_string()
	print "First 10 digits:", res.to_string_10()