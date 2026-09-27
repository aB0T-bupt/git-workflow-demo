import unittest

from greeting import greet


class GreetingTests(unittest.TestCase):
    def test_greets_a_name(self) -> None:
        self.assertEqual(greet("Alice"), "Hello, Alice!")

    def test_rejects_an_empty_name(self) -> None:
        self.assertEqual(greet(""), "Name cannot be empty.")


if __name__ == "__main__":
    unittest.main()
