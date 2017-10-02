#!/usr/bin/env python
#coding: utf-8

import math

def visit(A):
    n = len(A)
    h = int(math.log(n, 2)) + 1
    i = 0
    visted = []
    while i < h:
        h_visited = []
        start = 2**i - 1
        end = 2**(i+1) - 1
        j = start
        while j < end and j < n:
            h_visited.append(A[j])
            j = j + 1
        i = i + 1
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
        max_heapify(A, largest, heap_size)

def build_max_heap(A):
    n = len(A)
    i = n/2
    while i >= 0:
        max_heapify(A, i, n)
        i = i - 1

def heap_sort(A):
    build_max_heap(A)
    n = len(A)
    i = n - 1
    while i > 0:
        tmp = A[i]
        A[i] = A[0]
        A[0] = tmp
        max_heapify(A, 0, i)
        i = i - 1

def left(i):
    return 2*i+1

def right(i):
    return 2*(i+1)

def parent(i):
    return i/2
