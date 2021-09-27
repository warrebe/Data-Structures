# Course: CS261 - Data Structures
# Student Name: Benjamin Warren
# Assignment: Binary Search
# Description: Static Array Binary Search (source: canvas module example)

import random
import time
from static_array import *


# ------------------- PROBLEM 1 - -------------------------------------------


def binary_search(arr: StaticArray, target: int) -> int:
    """
    Binary search for a sorted static array
    :param arr: arr to search
    :param target: target to search for
    :return: Index found at
    """
    if arr.size() == 1:
        if arr[0] == target:
            return 0
        else:
            return -1
    if arr[0] < arr[1]:
        low = 0
        high = arr.size() - 1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                index = mid
                return index
            elif target < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return -1
    else:
        low = 0
        high = arr.size() - 1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                index = mid
                return index
            elif target > arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return -1


# ------------------- PROBLEM 2 - -------------------------------------------

def findPivot(arr, low, high):
    """
    Finds the picot point of a rotated list for the purposes of a binary search algorithm
    :param arr: Arr to find pivot of
    :param low: First index
    :param high: Max index
    :return: Pivot
    """
    if (high < low):
        return -1
    if (high == low):
        return low
    mid = (low + high) // 2
    if (mid < high and arr[mid + 1] < arr[mid]):
        return mid
    if (mid > low and arr[mid] < arr[mid - 1]):
        return mid - 1
    if (arr[low] > arr[mid]):
        return findPivot(arr, low, mid - 1)
    else:
        return findPivot(arr, mid + 1, high)

def binary_search_rotated(arr: StaticArray, target: int) -> int:
    """
    Find a target value using binary search on a sorted, yet rotated list
    :param arr: Rotated array to search
    :param target: Target value to find
    :return: Index location
    """
    low = 0
    high = arr.size() - 1
    mid = findPivot(arr, low, high)
    if arr[mid] == target:
        return mid
    elif arr[0] <= target < arr[mid]:
        low = 0
        high = mid - 1
    else:
        low = mid
        high = arr.size() - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            index = mid
            return index
        elif target < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1



# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":
    """
    print('\n# problem 1 example 1')
    src = (-10, -5, 0, 5, 7, 9, 11)
    targets = (7, -10, 11, 0, 8, 1, -100, 100)
    arr = StaticArray(len(src))
    for i, value in enumerate(src):
        arr[i] = value
    print([binary_search(arr, target) for target in targets])
    arr._data.reverse()
    print([binary_search(arr, target) for target in targets])


    print('\n# problem 1 example 2')
    src = [random.randint(-10 ** 7, 10 ** 7) for _ in range(5_000_000)]
    src = sorted(set(src))
    arr = StaticArray(len(src))
    arr._data = src[:]

    # add 20 valid and 20 (likely) invalid targets
    targets = [-10 ** 8, 10 ** 8]
    targets += [arr[random.randint(0, len(src) - 1)] for _ in range(20)]
    targets += [random.randint(-10 ** 7, 10 ** 7) for _ in range(18)]

    result, total_time = True, 0
    for target in targets:
        total_time -= time.time()
        answer = binary_search(arr, target)
        total_time += time.time()
        result &= arr[answer] == target if target in src else answer == -1
    print(result, total_time < 0.5)

    arr._data.reverse()
    for target in targets:
        total_time -= time.time()
        answer = binary_search(arr, target)
        total_time += time.time()
        result &= arr[answer] == target if target in src else answer == -1
    print(result, total_time < 0.5)
    """

    print('\n# problem 2 example 1')
    test_cases = (
        ((6, 8, 12, 20, 0, 2, 5), 0),
        ((6, 8, 12, 20, 0, 2, 5), -1),
        ((1,), 1),
        ((1,), 0),
    )
    result = []
    for src, target in test_cases:
        arr = StaticArray(len(src))
        for i, value in enumerate(src):
            arr[i] = value
        result.append((binary_search_rotated(arr, target)))
    print(*result)


    print('\n# problem 2 example 2')
    src = [random.randint(-10 ** 7, 10 ** 7) for _ in range(5_000_000)]
    src = sorted(set(src))
    arr = StaticArray(len(src))
    arr._data = src[:]

    # add 20 valid and 20 (likely) invalid targets
    targets = [-10 ** 8, 10 ** 8]
    targets += [arr[random.randint(0, len(src) - 1)] for _ in range(20)]
    targets += [random.randint(-10 ** 7, 10 ** 7) for _ in range(18)]

    result, total_time = True, 0
    for target in targets:
        # rotate arr random number of steps
        pivot = random.randint(0, len(src) - 1)
        arr._data = src[pivot:] + src[:pivot]

        total_time -= time.time()
        answer = binary_search_rotated(arr, target)
        total_time += time.time()
        result &= arr[answer] == target if target in src else answer == -1
    print(result, total_time < 0.5)

