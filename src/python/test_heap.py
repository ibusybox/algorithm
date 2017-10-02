#!/usr/bin/env python
#coding: utf-8

import unittest
import heap

class TestVisitHeap(unittest.TestCase):
    def setUp(self):
        print "start visit heap test"
    def tearDown(self):
        print "end visit heap test"
    def test_case01(self):
        A = [1,2,3]
        visit = heap.visit(A)
        print visit
        self.assertTrue(visit[0] == [1] and visit[1] == [2,3])

    def test_case02(self):
        A = [1,2,3,4]
        visit = heap.visit(A)
        print visit
        self.assertTrue(visit[0] == [1] and visit[1] == [2,3] and visit[2] == [4])

    def test_case03(self):
        A = [4,1,3,2,16,9,10,14,8,7]
        visit = heap.visit(A)
        print visit
        self.assertTrue(visit[0] == [4] and visit[1] == [1,3] and visit[2] == [2,16,9,10] and visit[3] == [14,8,7])
    
 

class TestMaxHeapify(unittest.TestCase):
    def setUp(self):
        print "start max heapify test"
    def tearDown(self):
        print "end max heapify test"
    def test_case01(self):
        A = [1,2,3]
        heap.max_heapify(A, 0, len(A))
        visit = heap.visit(A)
        self.assertTrue(visit[0] == [3] and visit[1] == [2,1])

    def test_case02(self):
        A = [1,2,3,4]
        heap.max_heapify(A, 1, len(A))
        visit = heap.visit(A)
        print visit
        self.assertTrue(visit[0] == [1] and visit[1] == [4,3] and visit[2] == [2])

class TestBuildMaxHeap(unittest.TestCase):
    def setUp(self):
        print "start build max heap test"
    def tearDown(self):
        print "end build max heap test"
    def test_case01(self):
        A = [1,2,3,4]
        heap.build_max_heap(A)
        visit = heap.visit(A)
        print visit
        self.assertTrue(visit[0] == [4] and visit[1] == [2,3] and visit[2] == [1])

    def test_case02(self):
        A = [4,1,3,2,16,9,10,14,8,7]
        heap.build_max_heap(A)
        visit = heap.visit(A)
        print visit
        self.assertTrue(visit[0] == [16] and visit[1] == [14,10] and visit[2] == [8,7,9,3] and visit[3] == [2,4,1])

class TestHeapSort(unittest.TestCase):
    def setUp(self):
        print "start heap sort test"
    def tearDown(self):
        print "end heap sort test"
    def test_case01(self):
        A = [2,3,1]
        heap.heap_sort(A)
        print A
        self.assertTrue(A == [1,2,3])

    def test_case02(self):
        A = [4,1,3,2,16,9,10,14,8,7]
        heap.heap_sort(A)
        print A
        self.assertTrue(A == [1,2,3,4,7,8,9,10,14,16])

if __name__ == '__main__':
    suit = unittest.TestSuite()
    suit.addTest(unittest.makeSuite(TestVisitHeap))
    suit.addTest(unittest.makeSuite(TestMaxHeapify))
    suit.addTest(unittest.makeSuite(TestBuildMaxHeap))
    suit.addTest(unittest.makeSuite(TestHeapSort))
    runner = unittest.TextTestRunner()
    runner.run(suit)