#!/usr/bin/env python
# -*- coding: utf-8 -*-


def naive(entries, name):
    """Searches the entries and returns the position of the name (positive)
    or -1 if name is not in name"""
    for i, e in enumerate(entries):
        if e.name == name:
            return i
    return -1


def binary_search(ordered_entries, name):
    """searches ordered_entries for name using binary search.
    Returns the index of the found element or negative"""
    low = 0
    high = len(ordered_entries) - 1
    while low <= high:
        mid = (low + high) / 2
        e = ordered_entries[mid]
        if name == e.name:
            return mid

        if name < e.name:
            high = mid - 1
        else:
            low = mid + 1

    return -(low + 1)

