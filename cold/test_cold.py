from cold import answer
import unittest 

class TestCold(unittest.TestCase):
	def test_answer(self) -> None:
        """_summary_
        """
		data = ‘-3 -454 0 454 -56565 - 45445’
		ans = answer(data)
		expected = 4 
		self.assertEqual(ans, expected)
	def test_answer1(self) -> None:
		""" """
		self.assertEqual(answer(‘23 32 6 566 7757’), 0)
	
	def solve() -> None:
        """_summary_
        """
		_ = input()
		data = input()
		print(answer(data))

	If__name__ == “__main__”
		solve()