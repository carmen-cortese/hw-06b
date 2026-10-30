# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    
    # My added tests for invalid inputs

    def testUpperBoundInvalid(self):
        # 201 in each position
        self.assertEqual(classifyTriangle(201, 100, 100), 'InvalidInput', '201,100,100 should be InvalidInput')
        self.assertEqual(classifyTriangle(100, 201, 100), 'InvalidInput', '100,201,100 should be InvalidInput')
        self.assertEqual(classifyTriangle(100, 100, 201), 'InvalidInput', '100,100,201 should be InvalidInput')
 
    def testUpperBoundValid(self):
        # 200 is the largest allowed value
        self.assertEqual(classifyTriangle(200, 200, 200), 'Equilateral', '200,200,200 should be Equilateral')
 
    # ---------- Input validation: lower bound (sides must be > 0) ----------
 
    def testZeroSides(self):
        # zero in each position
        self.assertEqual(classifyTriangle(0, 1, 1), 'InvalidInput', '0,1,1 should be InvalidInput')
        self.assertEqual(classifyTriangle(1, 0, 1), 'InvalidInput', '1,0,1 should be InvalidInput')
        self.assertEqual(classifyTriangle(1, 1, 0), 'InvalidInput', '1,1,0 should be InvalidInput')
 
    def testNegativeSides(self):
        # negative value in each position
        self.assertEqual(classifyTriangle(-1, 1, 1), 'InvalidInput', '-1,1,1 should be InvalidInput')
        self.assertEqual(classifyTriangle(1, -1, 1), 'InvalidInput', '1,-1,1 should be InvalidInput')
        self.assertEqual(classifyTriangle(1, 1, -1), 'InvalidInput', '1,1,-1 should be InvalidInput')
 
    def testLowerBoundValid(self):
        # 1 is the smallest allowed value
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral', '1,1,1 should be Equilateral')
 
    #Input validation: integers only
 
    def testFloatInputs(self):
        # float in each position
        self.assertEqual(classifyTriangle(1.5, 2, 2), 'InvalidInput', '1.5,2,2 should be InvalidInput')
        self.assertEqual(classifyTriangle(2, 1.5, 2), 'InvalidInput', '2,1.5,2 should be InvalidInput')
        self.assertEqual(classifyTriangle(2, 2, 1.5), 'InvalidInput', '2,2,1.5 should be InvalidInput')
 
    def testStringInputs(self):
        # string in each position
        self.assertEqual(classifyTriangle('a', 2, 2), 'InvalidInput', 'a,2,2 should be InvalidInput')
        self.assertEqual(classifyTriangle(2, 'b', 2), 'InvalidInput', '2,b,2 should be InvalidInput')
        self.assertEqual(classifyTriangle(2, 2, 'c'), 'InvalidInput', '2,2,c should be InvalidInput')
 
    #Triangle inequality
 
    def testNotATriangleDegenerate(self):
        # two sides add up to exactly the third: a flat line, not a triangle
        self.assertEqual(classifyTriangle(1, 2, 3), 'NotATriangle', '1,2,3 should be NotATriangle')
        self.assertEqual(classifyTriangle(3, 1, 2), 'NotATriangle', '3,1,2 should be NotATriangle')
        self.assertEqual(classifyTriangle(2, 3, 1), 'NotATriangle', '2,3,1 should be NotATriangle')
 
    def testNotATriangleTooShort(self):
        # two sides add up to less than the third, long side in each position
        self.assertEqual(classifyTriangle(1, 2, 10), 'NotATriangle', '1,2,10 should be NotATriangle')
        self.assertEqual(classifyTriangle(10, 1, 2), 'NotATriangle', '10,1,2 should be NotATriangle')
        self.assertEqual(classifyTriangle(2, 10, 1), 'NotATriangle', '2,10,1 should be NotATriangle')
 
    #Classification
 
    def testEquilateralTriangles(self):
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral', '1,1,1 should be Equilateral')
        self.assertEqual(classifyTriangle(5, 5, 5), 'Equilateral', '5,5,5 should be Equilateral')
        self.assertEqual(classifyTriangle(200, 200, 200), 'Equilateral', '200,200,200 should be Equilateral')
 
    def testIsocelesTriangles(self):
        # the odd side in each position
        self.assertEqual(classifyTriangle(5, 5, 3), 'Isoceles', '5,5,3 should be Isoceles')
        self.assertEqual(classifyTriangle(5, 3, 5), 'Isoceles', '5,3,5 should be Isoceles')
        self.assertEqual(classifyTriangle(3, 5, 5), 'Isoceles', '3,5,5 should be Isoceles')
 
    def testScaleneTriangles(self):
        # valid, non-right, all sides different, in different orders
        self.assertEqual(classifyTriangle(4, 5, 6), 'Scalene', '4,5,6 should be Scalene')
        self.assertEqual(classifyTriangle(6, 4, 5), 'Scalene', '6,4,5 should be Scalene')
        self.assertEqual(classifyTriangle(5, 6, 4), 'Scalene', '5,6,4 should be Scalene')
 
    def testRightTriangles(self):
        # the hypotenuse in each position, plus a second right triangle
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right', '3,4,5 should be Right')
        self.assertEqual(classifyTriangle(5, 3, 4), 'Right', '5,3,4 should be Right')
        self.assertEqual(classifyTriangle(4, 5, 3), 'Right', '4,5,3 should be Right')
        self.assertEqual(classifyTriangle(5, 12, 13), 'Right', '5,12,13 should be Right')
        self.assertEqual(classifyTriangle(13, 5, 12), 'Right', '13,5,12 should be Right')
 
#Original tests from the asssignment
    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

