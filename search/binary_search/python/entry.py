#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Entry(object):

    __slots__ = ('name', 'phone')

    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def __repr__(self):
        return "%s\t%s" % (self.name, self.phone)

    @classmethod
    def fromline(cls, line):
        """return an instance of the entry in that line"""
        line = line.strip(' \r\n')
        name, phone = line.split('\t')
        return cls(name, phone)

