#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import sys

from entry import Entry
import search
from bst import BinarySearchTree


def main():

    name = sys.argv[1];

    for i in xrange(1, 11):
        fname = '../data/%d_catalog.txt' % i
        #read the catalog and load to a list
        phonebook = []
        append = phonebook.append

        with open(fname, 'r') as f:
            for l in f:
                if l:
                    append(Entry.fromline(l))

        #print 'phonebook contains %d entries' % len(phonebook)
        name_idx = BinarySearchTree()
        for i, e in enumerate(phonebook):
            name_idx.add(e.name, i)

        start = time.time()
        idxs = name_idx.get(name)
        bstelapsed = (time.time() - start) * 1000

        # let's sort the entries by name
        phonebook.sort(key=lambda e: e.name)

        # let' search for a non existing name using naive search
        start = time.time()
        idx = search.naive(phonebook, name)
        nelapsed = (time.time() - start) * 1000

        # the same using binary search
        bstart = time.time()
        idx = search.binary_search(phonebook, name)
        bselapsed = (time.time() - bstart) * 1000
        print '%d - naive: %g - binary: %g - bst: %g'\
              % (len(phonebook), nelapsed, bselapsed, bstelapsed)




if __name__ == '__main__':

    main()

