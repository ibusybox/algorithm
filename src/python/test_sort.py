#!/usr/bin/env python
#coding: utf-8

import unittest
import sort

class TestInsertionSort(unittest.TestCase):
    def setUp(self):
        print "start insertion sort test"
    def tearDown(self):
        print "end insertion sort test"
    def test_case01(self):
        A = [3,2,1]
        print "origin A=%s" % A
        sort.insertion_sort(A)
        print "insertion sorted A=%s" % A
        self.assertTrue([1,2,3] == A)
    def test_case02(self):
        A = [3,1]
        print "origin A=%s" % A
        sort.insertion_sort(A)
        print "insertion sorted A=%s" % A
        self.assertTrue([1,3] == A)
    def test_case03(self):
        A = [3,4,5,2,1]
        print "origin A=%s" % A
        sort.insertion_sort(A)
        print "insertion sorted A=%s" % A
        self.assertTrue([1,2,3,4,5] == A)

class TestSelectionSort(unittest.TestCase):
    def setUp(self):
        print "start selection sort test"
    def tearDown(self):
        print "end selection sort test"
    def test_case01(self):
        A = [3,2,1]
        print "origin A=%s" % A
        sort.selection_sort(A)
        print "selection sorted A=%s" % A
        self.assertTrue([1,2,3] == A)
    def test_case02(self):
        A = [3,1]
        print "origin A=%s" % A
        sort.selection_sort(A)
        print "selection sorted A=%s" % A
        self.assertTrue([1,3] == A)
    def test_case03(self):
        A = [3,4,5,2,1]
        print "origin A=%s" % A
        sort.selection_sort(A)
        print "selection sorted A=%s" % A
        self.assertTrue([1,2,3,4,5] == A)

class TestBubbleSort(unittest.TestCase):
    def setUp(self):
        print "start bubble sort test"
    def tearDown(self):
        print "end bubble sort test"
    def test_case01(self):
        A = [3,2,1]
        print "origin A=%s" % A
        sort.bubble_sort(A)
        print "bubble sorted A=%s" % A
        self.assertTrue([1,2,3] == A)
    def test_case02(self):
        A = [3,1]
        print "origin A=%s" % A
        sort.bubble_sort(A)
        print "bubble sorted A=%s" % A
        self.assertTrue([1,3] == A)
    def test_case03(self):
        A = [3,4,5,2,1]
        print "origin A=%s" % A
        sort.bubble_sort(A)
        print "bubble sorted A=%s" % A
        self.assertTrue([1,2,3,4,5] == A)

class TestMergeSort(unittest.TestCase):
    def setUp(self):
        print "start merge sort test"
    def tearDown(self):
        print "end merge sort test"
    def test_case01(self):
        A = [3,2,1]
        print "origin A=%s" % A
        sort.merge_sort(A, 0, len(A))
        print "merge sorted A=%s" % A
        self.assertTrue([1,2,3] == A)
    def test_case02(self):
        A = [3,1]
        print "origin A=%s" % A
        sort.merge_sort(A, 0, len(A))
        print "merge sorted A=%s" % A
        self.assertTrue([1,3] == A)
    def test_case03(self):
        A = [3,4,5,2,1]
        print "origin A=%s" % A
        sort.merge_sort(A, 0, len(A))
        print "merge sorted A=%s" % A
        self.assertTrue([1,2,3,4,5] == A)

        
if __name__ == '__main__':
    suit = unittest.TestSuite()
    suit.addTest(unittest.makeSuite(TestSelectionSort))
    suit.addTest(unittest.makeSuite(TestInsertionSort))
    suit.addTest(unittest.makeSuite(TestBubbleSort))
    suit.addTest(unittest.makeSuite(TestMergeSort))
    runner = unittest.TextTestRunner()
    runner.run(suit)
