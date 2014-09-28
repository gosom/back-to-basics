# Binary Search

I wil build a class representing each telephone book entry.

The implementation for each language is to the corresponding folder.
In that folder there is also a result.txt file which contains the time needed
to search for a non existing element (this is the worst case)

Results for python

(first column is input size)

```
1000 - naive: 0.516176 - binary: 0.0269413 - position: -1001
2000 - naive: 0.398874 - binary: 0.0109673 - position: -2001
4000 - naive: 0.763893 - binary: 0.0100136 - position: -4001
8000 - naive: 1.43194 - binary: 0.0112057 - position: -8001
16000 - naive: 3.13187 - binary: 0.0140667 - position: -16001
32000 - naive: 8.075 - binary: 0.0150204 - position: -32001
64000 - naive: 19.1159 - binary: 0.0178814 - position: -64001
128000 - naive: 39.8681 - binary: 0.0188351 - position: -128001
256000 - naive: 80.9479 - binary: 0.0181198 - position: -256001
512000 - naive: 164.571 - binary: 0.0197887 - position: -512001

```

You can clearly see that the naive implementation is much more slower,
and it get's worse when we have more entries. Actually the time needed gets
doubled when we double the input size ( 0(n) complexity).

The binary search performs almost the same no matter the phonebook size
( O(log(n) complexity) )

C++ implementation behaves similarly.

How to run:

```python main.py "string to search"```

For c++ compile:

```g++ --std=c++11 Entry.cpp search.cpp main.cpp -o search```

* C++ requires boost library (uses string split method)


Standard Library Implementations:

    - For python check the [bisect](https://docs.python.org/2/library/bisect.html)
    module.

    - In c++ there is the [std::binary_search](http://en.cppreference.com/w/cpp/algorithm/binary_search)

