#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
BinarySearchTree Implementation
Delete operation is not implemented

See Usage:

>>> b = BinarySearchTree()
>>> b = BinarySearchTree()
>>>
>>> b.add('wow', 1)
>>> b.add('awesome', 2)
>>> b.add('vacation', 12)
>>> b.add('work', 13)
>>> 'wow' in b
True
>>> 'not' in b
False
>>> b.get('vacation')
[12]
>>> list(b.__iter__())
['awesome', 'vacation', 'work', 'wow']

"""


class Node(object):

    def __init__(self, key, value):
        self.key = key
        self.left = None
        self.right = None
        self.data = []
        self.data.append(value)

    def __iter__(self):
        if self.left:
            for n in self.left:
                yield n

        yield self.key

        if self.right:
            for n in self.right:
                yield n

    def add(self, key, value):
        if key == self.key:
            self.data.append(value)
        elif key < self.key:
            if self.left:
                self.left.add(key, value)
            else:
                self.left = Node(key, value)
        else:
            if self.right:
                self.right.add(key, value)
            else:
                self.right = Node(key, value)

class BinarySearchTree(object):

    def __init__(self):
        self.root = None

    def add(self, key, value):
        if not self.root:
            self.root = Node(key, value)
        else:
            self.root.add(key, value)

    def get(self, key):
        if not self.root:
            return None

        node = self._get(key, self.root)
        return node.data if node else None

    def _get(self, key, node):
        if not node:
            return None

        if key == node.key:
            return node

        if key < node.key:
            return self._get(key, node.left)

        if key > node.key:
            return self._get(key, node.right)

    def __contains__(self, key):
        if not self.root:
            return False

        return True if self._get(key, self.root) else False

    def __iter__(self):
        return self.root.__iter__()
