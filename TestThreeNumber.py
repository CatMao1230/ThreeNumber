import ThreeNumber
import unittest

class TestThreeNumber(unittest.TestCase):
	def test_access_from_file(self):
		file_name = "arr.dat"
		expacted_value = ['2134', '3412', '6421', '8723', '9239', '1234', '2345']
		value = ThreeNumber.access_from_file(file_name)
		self.assertEqual(expacted_value, value)
	def test_find_three_max_1(self):
		number = [400, 100, 50, 30, 300, 200, 10]
		expacted_value = [400, 300, 200]
		value = ThreeNumber.find_three_max(number)
		self.assertEqual(expacted_value, value)
	def test_find_three_max_2(self):
		number = []
		expacted_value = [0, 0, 0]
		value = ThreeNumber.find_three_max(number)
		self.assertEqual(expacted_value, value)

if __name__ == '__main__':
	unittest.main()
