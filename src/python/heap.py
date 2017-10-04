#!/usr/bin/env python
#coding: utf-8

import math

def visit(A):
    n = len(A)
    height = int(math.log(n, 2)) + 1
    h = 0
    visted = []
    while h < height:
        h_visited = []
        start = 2**h - 1
        end = 2**(h+1) - 1
        j = start
        while j < end and j < n:
            h_visited.append(A[j])
            j = j + 1
        h = h + 1
        visted.append(h_visited)
    return visted

def max_heapify(A, i, heap_size):
    l = left(i)
    r = right(i)
    largest = i
    if l < heap_size and A[i] < A[l]:
        largest = l
    if r < heap_size and A[r] > A[largest]:
        largest = r
    # swap A[i] and A[largest]
    if largest != i:
        tmp = A[largest]
        A[largest] = A[i]
        A[i] = tmp
        # make sure heap A start with largest is a maximum heap
        max_heapify(A, largest, heap_size)

def build_max_heap(A):
    n = len(A)
    i = n/2
    # array index start with n/2 is leaf nodes in a heap
    # so make sure each parent is maxinum heap
    while i >= 0:
        max_heapify(A, i, n)
        i = i - 1

def heap_sort(A):
    build_max_heap(A)
    n = len(A)
    heap_size = n - 1
    while heap_size > 0:
        tmp = A[heap_size]
        A[heap_size] = A[0]
        A[0] = tmp
        max_heapify(A, 0, heap_size)
        heap_size = heap_size - 1

def left(i):
    return 2*i+1

def right(i):
    return 2*(i+1)

def parent(i):
    return i/2
