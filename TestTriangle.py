# -*- coding: utf-8 -*-


import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self):
        self.assertEqual(classifyTriangle(3,4,5),'Right')

    def testRightTriangleB(self):
        self.assertEqual(classifyTriangle(4,5,3),'Right')

    def testEquilateralTriangleA(self):
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral')

    def testEquilateralTriangleB(self):
        self.assertEqual(classifyTriangle(22,22,22),'Equilateral')

    def testScaleneTriangleA(self):
        self.assertEqual(classifyTriangle(6,7,8),"Scalene")

    def testScaleneTriangleB(self):
        self.assertEqual(classifyTriangle(33,12,34), "Scalene")

    def testIsoscelesTriangle(self):
        self.assertEqual(classifyTriangle(3,3,5),'Isosceles')

    def testNotATriangle(self):
        self.assertEqual(classifyTriangle(7, 3, 2), "NotATriangle")

    def testInvalidInputs(self):
        self.assertEqual(classifyTriangle(2002, 22, 4), "InvalidInput")

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
