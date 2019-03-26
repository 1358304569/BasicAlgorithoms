# coding:utf-8

import random

def Merge(nums, l, m, r):
    left = []
    right = []
    n1 = m - l +1
    n2 = r - m
    for i in range(n1):
        left.append(nums[l + i])

    for j in range(n2):
        right.append(nums[m + 1 + j])
    i = 0
    j = 0
    k = l

    while i < n1 and j < n2:
        if left[i] <= right[j]:
            nums[k] = left[i]
            i += 1
        else:
            nums[k] = right[j]
            j += 1
        k += 1

    while i < n1:
        nums[k] = left[i]
        i += 1
        k += 1

    while j < n2:
        nums[k] = right[j]
        j += 1
        k += 1




def MergeSort(nums, l, r):
    if l < r:
        m = l + int((r - l)/2)
        MergeSort(nums, l, m)
        MergeSort(nums, m+1, r)
        Merge(nums, l, m, r)

nums = [x*10 for x in range(1,11)]
random.shuffle(nums)
# nums = [10, 80, 50, 70, 100, 60, 90, 30, 40, 20]
print(nums)
MergeSort(nums, 0, len(nums)-1)
print(nums)


