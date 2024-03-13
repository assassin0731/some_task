import unittest

from lib import Circle, Triangle


class Tests(unittest.TestCase):

    def test_triangle_1(self):
        triangle = Triangle([3, 4, 5])
        self.assertEqual(triangle.calculate(), 6)
        self.assertEqual(triangle.check_right_angled(), "Треугольник прямоугольный")

    def test_triangle_2(self):
        triangle = Triangle([4, 5, 6])
        self.assertAlmostEqual(triangle.calculate(),  9.92156, places=4)
        self.assertEqual(triangle.check_right_angled(), "Треугольник не прямоугольный")

    def test_circle_1(self):
        circle = Circle([4])
        self.assertAlmostEqual(circle.calculate(),  50.26548, places=4)

    def test_circle_2(self):
        circle = Circle([10])
        self.assertAlmostEqual(circle.calculate(),  314.15926, places=4)


if __name__ == "__main__":
    unittest.main()
