#! /usr/bin/python
# -*- coding: utf-8 -*-

# Python program for implementation of heap Sort
import argparse
from math import floor


def HEAPSORT(A):
    heapSize = len(A)
    BUILDMAXHEAP(A,heapSize)
    for i in range (heapSize,1,-1):
        A[0],A[i-1] = A[i-1],A[0]
        heapSize = heapSize - 1
        MAXHEAPIFY(A,1,heapSize)
# end HEAPSORT

def BUILDMAXHEAP(A,hS):
    for i in range(floor(hS/2),0,-1):
        MAXHEAPIFY(A,i,hS)
# end BUILD-MAX-HEAP

def MAXHEAPIFY(A,i,hS):
    l = 2*i
    r = 2*i+1

    if l <= hS and A[l-1] > A[i-1]:
        largest = l
    else: largest = i
    
    if r <= hS and A[r-1] > A[largest-1]:
        largest = r
        
    if largest != i:
        A[i-1],A[largest-1] = A[largest-1],A[i-1]
        MAXHEAPIFY(A,largest,hS)
# end MAX-HEAPIFY

def READDATAFILE(nums):
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", help="Nombre del archivo a procesar.")
    args = parser.parse_args()

    if args.file:
        print("El nombre del archivo a procesar es: ", args.file)
    
    file = open(args.file)
    data = file.read()
    
    for word in data.split():
        nums.append(int(word))
# end READDATAFILE

    
def main():
    nums = []
    READDATAFILE(nums)
    HEAPSORT(nums)

main()

