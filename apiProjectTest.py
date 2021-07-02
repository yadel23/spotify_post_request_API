import unittest
from apiProject import user_inputLink

class TestFileName(unittest.TestCase):
    def test_function1(self):
        self.assertTrue(len(user_inputLink()) > 5)
      

if __name__ == '__main__':
    unittest.main()