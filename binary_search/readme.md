Binary Search
==============


Let's assume we have some files that represent telephone catalogs.
We want to be able to locate if a name exists on the catalog.
We also need to be able to locate if a telephone exists on the catalog.

File build-demo-data.py will be used to generate telephone catalogs of
different sizes.

The catalogs are in the folder data and named catalog1.txt, ..., catalog10.txt.

I wil build a class representing each telephone book entry.

The implementation for each language is to the corresponding folder.
In that folder there is also a result.txt file which contains the time needed
to search for a non existing element (this is the worst case)

Results for python

```
1000 - naive: 0.388861 - binary: 0.0200272
2000 - naive: 0.48995 - binary: 0.013113
4000 - naive: 0.865936 - binary: 0.0119209
8000 - naive: 1.48797 - binary: 0.0109673
16000 - naive: 3.72696 - binary: 0.0138283
32000 - naive: 8.04996 - binary: 0.014782
64000 - naive: 19.0718 - binary: 0.0150204
128000 - naive: 40.699 - binary: 0.0171661
256000 - naive: 80.7359 - binary: 0.0190735
512000 - naive: 164.494 - binary: 0.0188351
```

You can clearly see that the naive implementation is much more slower,
and it get's worse when we have more entries. Actually the time needed gets
doubled when we double the input size ( 0(n) complexity).

The binary search performs almost the same no matter the phonebook size
( O(log(n) complexity) )
