#!/usr/bin/env python
#coding: utf-8

import random

def premute_sorting(A):
    n = len(A)
    P = []
    i = 0
    while i < n:
        P.append(random.randint(0, n**3))
        i = i + 1

    i = 0
    while i < n:
        min = P[i]
        k = i
        j = i + 1
        while j < n:
            if P[j] < min:
                min = P[j]
                k = j
            j = j + 1
        tmp = P[i]
        P[i] = P[k]
        P[k] = tmp

        tmp = A[i]
        A[i] = A[k]
        A[k] = tmp
        
        i = i + 1


def premute_inplace(A):
    n = len(A)
    i = 0
    while i < n:
        j = random.randint(i, n-1)
        tmp = A[i]
        A[i] = A[j]
        A[j] = tmp
        i = i + 1 