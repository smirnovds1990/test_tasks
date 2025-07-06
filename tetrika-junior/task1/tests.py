import unittest

from solution import sum_two


class TestStrictDecorator(unittest.TestCase):

    def test_with_right_args(self):
        self.assertEqual(sum_two(1, 2), 3)

    def test_with_right_kwargs(self):
        self.assertEqual(sum_two(a=1, b=2), 3)

    def test_with_right_arg_and_kwarg(self):
        self.assertEqual(sum_two(1, b=2), 3)

    def test_with_wrong_args(self):
        with self.assertRaises(TypeError):
            sum_two(1, 2.4)

    def test_with_wrong_kwargs(self):
        with self.assertRaises(TypeError):
            sum_two(a=1.0, b=2)

    def test_with_wrong_arg_and_kwarg(self):
        with self.assertRaises(TypeError):
            sum_two(1, b=2.8)


if __name__ == "__main__":
    unittest.main()
