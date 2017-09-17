#!/usr/bin/env python
#coding: utf-8

import unittest
import premute
import copy

class TestPremuteSorting(unittest.TestCase):
    def setUp(self):
        print "start premute sorting test"
    def tearDown(self):
        print "end premute sorting test"
    def test_case01(self):
        A = [1,2,3]
        A1 = copy.copy(A)
        A2 = copy.copy(A)
        A3 = copy.copy(A)
        premute.premute_sorting(A1)
        premute.premute_sorting(A2)
        premute.premute_sorting(A3)
        print "A=%s, A1=%s, A2=%s, A3=%s" % (A, A1, A2, A3)
        self.assertTrue(A1 != A2 != A3)

class TestPremuteInplace(unittest.TestCase):
    def setUp(self):
        print "start premute inplace test"
    def tearDown(self):
        print "end premute inplace test"
    def test_case01(self):
        A = [1,2,3]
        A1 = copy.copy(A)
        A2 = copy.copy(A)
        A3 = copy.copy(A)
        premute.premute_inplace(A1)
        premute.premute_inplace(A2)
        premute.premute_inplace(A3)
        print "A=%s, A1=%s, A2=%s, A3=%s" % (A, A1, A2, A3)
        self.assertTrue(A1 != A2 != A3)

if __name__ == '__main__':
    suit = unittest.TestSuite()
    suit.addTest(unittest.makeSuite(TestPremuteSorting))
    suit.addTest(unittest.makeSuite(TestPremuteInplace))
    runner = unittest.TextTestRunner()
    runner.run(suit)
