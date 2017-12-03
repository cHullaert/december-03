import unittest

from spirale import Spirale

class TestSpirale(unittest.TestCase):

    def test_position(self):
        spirale=Spirale()
        self.assertEqual(spirale.get_position(1), (0, 0))

    def test_position12(self):
        spirale=Spirale()
        self.assertEqual(spirale.get_position(12), (1, 2))

    def test_position23(self):
        spirale=Spirale()
        self.assertEqual(spirale.get_position(23), (0, -2))

    def test_distanceTo1Is0(self):
        spirale=Spirale()
        self.assertEqual(spirale.get_distance(1), 0)

    def test_distanceTo12Is3(self):
        spirale=Spirale()
        self.assertEqual(spirale.get_distance(12), 3)

    def test_distanceTo23Is2(self):
        spirale=Spirale()
        self.assertEqual(spirale.get_distance(23), 2)

    def test_distanceTo1024Is31(self):
        spirale=Spirale()
        self.assertEqual(spirale.get_distance(1024), 31)
        
if __name__ == '__main__':
    unittest.main()