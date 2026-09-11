"""
CSAPX Lab 3: Tripods

Implementation of a hybrid sorting algorithm combining Merge Sort and Insertion Sort.

Applies recursive Merge Sort for larger datasets and switches to Insertion Sort
when sub-list sizes fall at or below a specified threshold (k).

author: YOUR NAME HERE
"""
from tripod import Tripod


def insertion_sort(data: list[Tripod]):
    if len(data) <= 1:
        return
    for i in range(1, len(data)):
        j = i - 1
        while data[i].sum < data[j].sum and j >= 0 and i >= 0:
            data[i], data[j] = data[j], data[i]
            i -= 1
            j -= 1


def merge(left: list[Tripod], right: list[Tripod]):
    merged = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i].sum < right[j].sum:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    if i == len(left):
        merged.extend(right[j:])
    elif j == len(right):
        merged.extend(left[i:])
    return merged


def hybrid_sort(data: list[Tripod], k: int) -> list[Tripod]:
    if len(data) <= k:
        insertion_sort(data)
        return data
    if len(data) <= 1:
        return data
    half = len(data) // 2
    left = hybrid_sort(data[:half], k)
    right = hybrid_sort(data[half:], k)
    return merge(left, right)
