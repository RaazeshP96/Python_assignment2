'''

Write a function, is_prime, that takes an integer and returns True if
the number is prime and False if the number is not prime.

'''
import unittest


def is_prime(num):
    s = 0
    for i in range(1, num+1):
        if num % i == 0:
            s += 1
    return True if s == 2 else False


print(is_prime(8))
print(is_prime(5))


class IsPrimeTest(unittest.TestCase):
    def test_pass(self):
        self.assertEqual(is_prime(8), False)
        self.assertEqual(is_prime(1), False)
        self.assertEqual(is_prime(5), True)


if __name__ == "__main__":
    unittest.main()
