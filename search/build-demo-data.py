#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import forgery_py


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('-i', dest='init_size', type=int, default=1000,
                        help='The initial number of entries.DEFAULT 1000')
    parser.add_argument('-s', dest='num', type=int, default=10,
                        help='How many catalogs to build. Each one has'
                        ' double number of elements than the previous.'
                        'DEFAULT 10')
    parser.add_argument('-f', dest='fname', default='data/%d_catalog.txt',
                        help='The filename to store the catalogs.'
                        'DEFAULT catalog%%d.txt')

    args = parser.parse_args()

    num_entries = args.init_size

    for i in xrange(1, args.num+1):
        catalog = args.fname % i
        with open(catalog, 'w') as f:
            for _ in xrange(num_entries):
                name = forgery_py.forgery.name.full_name()
                phone = forgery_py.forgery.address.phone()
                print >> f, name + '\t' + phone

        num_entries *= 2


if __name__ == '__main__':

    main()
