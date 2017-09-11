#!/usr/bin/env python
#coding: utf-8

def insertion_sort(A):
    n = len(A)
    if n < 2:
        return
    i = 0
    while i < n:
        j = i - 1
        next = A[i]
        while j >= 0 and A[j] > next:
            A[j+1] = A[j]
            j = j - 1
        A[j+1] = next
        i = i + 1

def selection_sort(A):
    n = len(A)
    if n < 2:
        return
    i = 0
    while i < n:
        min = A[i]
        k = i
        j = i + 1
        while j < n:
            if A[j] < min:
                min = A[j]
                k = j
            j = j + 1
        tmp = A[i]
        A[i] = A[k]
        A[k] = tmp
        i = i + 1
        
def bubble_sort(A):
    n = len(A)
    if n < 2:
        return
    i = 0
    while i < n:
        j = i
        while j < n:
            if A[i] > A[j]:
                tmp = A[i]
                A[i] = A[j]
                A[j] = tmp
            j = j + 1
        i = i + 1

def _merge(A, p, r, q):
    left = A[p:r]
    right = A[r:q]
    # 结束标记
    left.append(None)
    right.append(None)
    k = p
    i = j = 0
    while k < q:
        if left[i] is None and right[j] is not None:
            A[k] = right[j]
            j = j + 1
            k = k + 1
            continue
        if right[j] is None and left[i] is not None:
            A[k] = left[i]
            i = i + 1
            k = k + 1
            continue
        if left[i] < right[j]:
            A[k] = left[i]
            i = i + 1
        else:
            A[k] = right[j]
            j = j + 1      
        k = k + 1

def merge_sort(A, p, q):
    if q - p > 1:
        r = (p + q)/2
        merge_sort(A, p, r)
        merge_sort(A, r, q)
        _merge(A, p, r, q)