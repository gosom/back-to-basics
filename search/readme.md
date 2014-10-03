# Search

Let's assume we have some files that represent telephone catalogs.
We want to be able to find the telephone given a name in a catalog

File build-demo-data.py will be used to generate telephone catalogs of
different sizes.

The catalogs are in the folder data and named catalog1.txt, ..., catalog10.txt.

I am going to use 3 methods to locate a phone

- naive search
    Here we gonna iterate one by one all the names until we find the name we
    are looking for => O(N) complexity where N is the number of entries in the
    catalog.

- binary search
    We will use the binary seach algorithm as described here:
    http://en.wikipedia.org/wiki/Binary_search_algorithm
    complexity O(logn)

- binary search tree:
    We will create an index using a binary search tree i.e
    we will store the entries in random access data structure (list in python,
    vector in C++) and we will create a binary search tree with the
    entries and the position in that the appear in the data structure.
    Let's see an example:

        l = [entry1, entry2, entry3, entry4]
        The binary search tree will contain the information:
        entry_with_name_W = 0
        entry_with_name_X = 1
        entry_with_name_Y = 2
        entry_with_name_Z = 3
    At the best case we can get 0(logn) perfomance (if tree balanced)

## Comparison

