'''
    Write an if statement to determine whether a variable holding a year
    is a leap year.

'''
import unittest


def leapYear(year):
    return True if year % 4 == 0 else False

year=int(input("Enter the year:"))
print(leapYear(year))



class TestLeapYear(unittest.TestCase):

    def passTest(self):
        self.assertEqual(leapYear(2010), False)
        self.assertEqual(leapYear(2012), True)


if __name__ == "__main__":
    unittest.main()
