"""
CSAPX Lab 3: Tripods

Implementation of a hybrid sorting algorithm combining Merge Sort and Insertion Sort.

Applies recursive Merge Sort for larger datasets and switches to Insertion Sort
when sub-list sizes fall at or below a specified threshold (k).

author: Justin Spadone
"""
from tripod import Tripod

DEFAULT_K: int = 15


def insertion_sort(data: list[Tripod]):
    if len(data) <= 1:
        return
    for i in range(1, len(data)):
        j = i - 1
        key = data[i]
        while j >= 0 and key.sum < data[j].sum:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key


def merge(left: list[Tripod], right: list[Tripod]):
    merged = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i].sum <= right[j].sum:
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


def hybrid_sort(data: list[Tripod], k: int = DEFAULT_K) -> list[Tripod]:
    if len(data) <= k:
        insertion_sort(data)
        return data
    if len(data) <= 1:
        return data
    half = len(data) // 2
    left = hybrid_sort(data[:half], k)
    right = hybrid_sort(data[half:], k)
    return merge(left, right)
