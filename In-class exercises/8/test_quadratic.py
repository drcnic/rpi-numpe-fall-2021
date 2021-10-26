"""Template for Lesson 08 In-Class Exercise on testing"""

from quadratic import quadratic_roots
import unittest

class TestQuadratic(unittest.TestCase):

    def test_no_roots(self):
        """check that an empty list is returned when no solution"""
        roots = quadratic_roots(1., 0., 1.)
        self.assertTrue(len(roots)==0)

    def test_one_root(self):
        """test when quadratic has only one solution"""
        roots = quadratic_roots(1.,0.,0.)
        self.assertTrue(len(roots)==1)
        #self.assertAlmostEqual(0., roots[0], places=12)

    def test_two_roots(self):
        """test when quadratic has two solutions"""
        roots = quadratic_roots(1.,-1.,0.)
        self.assertAlmostEqual(0., roots[0], places=12)
        self.assertAlmostEqual(1., roots[1], places=12)

if __name__ == '__main__':
    unittest.main()
