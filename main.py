import unittest

def callRomanGuard(n):
    if type(n) != type(1):
        raise TypeError("Expected integer, got %s" % type(n))
    if (not 0 < n < 4000):
	    raise ValueError("Argument must be between 1 and 3999")

def toRoman(n):
	callRomanGuard(n)
	if (n < 4):
	    return "" + "I" * (n % 5) # 'I' * n
	if (n == 4):
	    return "IV"
	if (4 < n < 9):
	    return "V" + "I" * (n % 5)
	if (n == 9):
		return "IX"
	if (9 < n < 14):
		return "X" + "I" * (n % 5)
	if (n == 14):
		return "XIV"
	if (14 < n < 19):
		return "X" + "V" + "I" * (n % 5)

class ToRomanNumerals(unittest.TestCase):

    def testInputType(self):
	    self.assertRaises(TypeError, toRoman, "")

    def testLowerRange(self):
	    self.assertRaises(ValueError, toRoman, 0)

    def testUpperRange(self):
        self.assertRaises(ValueError, toRoman, 4000)

    def testOne(self):
        self.assertEqual("I", toRoman(1))

    def testTwo(self):
        self.assertEqual("II", toRoman(2))

    def testFour(self):
        self.assertEqual("IV", toRoman(4))

    def testFive(self):
        self.assertEqual("V", toRoman(5))

    def testSix(self):
        self.assertEqual("VI", toRoman(6))

    def testNine(self):
        self.assertEqual("IX", toRoman(9))

    def testTen(self):
        self.assertEqual("X", toRoman(10))

    def testEleven(self):
        self.assertEqual("XI", toRoman(11))

    def testFourteen(self):
        self.assertEqual("XIV", toRoman(14))

    def testFifteen(self):
        self.assertEqual("XV", toRoman(15))

    def testSixteen(self):
        self.assertEqual("XVI", toRoman(16))

def main():
    unittest.main()

if __name__ == '__main__':
    main()
