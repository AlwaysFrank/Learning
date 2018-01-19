#!/usr/bin/pythoon3
#-*-coding:UTF-8-*-

def quicksort(L):
    qsort(L, 0, len(L) - 1)
    return L


def qsort(L, first, last):
    if first < last:
        split = partition(L, first, last)
        qsort(L, first, split - 1)
        qsort(L, split + 1, last)

def partition(L, first, last):
    #choose first element as pivot
    pivot = L[first]
    left = first + 1
    right = last
    while True:
        while L[left] <= pivot:
            if left == right:
                break
            left += 1

        while L[right] > pivot:
            right -= 1

        if left < right:
            L[left], L[right] = L[right], L[left]
        else:
            break

    L[first], L[right] = L[right], L[first]
    return right

#test
origin = [2,0,1,8,0,1,1,9,-5,5]
print('before :',origin)
quicksort(origin)
print('after :',origin)