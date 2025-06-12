import unittest
from main import load_penguin_data

class TestPenguinData(unittest.TestCase):
    def test_load_penguin_data(self):
        shape = load_penguin_data()
        self.assertEqual(shape[1], 7)

if __name__ == '__main__':
    unittest.main()


