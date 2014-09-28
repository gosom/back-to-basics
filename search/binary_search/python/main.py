#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import sys

from entry import Entry
import search


def main():

    name = sys.argv[1];

    for i in xrange(1, 11):
        fname = '../../data/%d_catalog.txt' % i
        #read the catalog and load to a list
        phonebook = []
        append = phonebook.append

        with open(fname, 'r') as f:
            for l in f:
                if l:
                    append(Entry.fromline(l))

        #print 'phonebook contains %d entries' % len(phonebook)

        # let's sort the entries by name
        phonebook.sort(key=lambda e: e.name)

        # let' search for a non existing name using naive search
        start = time.time()
        idx = search.naive(phonebook, name)
        end = (time.time() - start) * 1000

        # the same using binary search
        bstart = time.time()
        idx = search.binary_search(phonebook, name)
        bend = (time.time() - bstart) * 1000

        print '%d - naive: %g - binary: %g - position: %s'\
              % (len(phonebook), end, bend, idx)


if __name__ == '__main__':

    main()

