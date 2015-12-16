# -*- coding: utf-8 -*-
__author__ = 'maito'
__all__ = ['add2zip_list']

import sys
import argparse
from bs4 import BeautifulSoup

def __read_postal_csv(postal_file_path):
    pass

def add2zip_list(args):
    """
    >>> add2zip_list(args)
    """
    __read_postal_csv(args['postal_file_path'])
    # address = args['address']


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument(
        '-a',
        dest = 'address',
        required = True,
        help='address to get zip code')
    parser.add_argument(
        '-f',
        dest = 'postal_file_path',
        nargs='?',
        default='../data/KEN_ALL_ROME.CSV',
        help='file path of postal code list KEN_ALL_ROME.CSV "http://www.post.japanpost.jp/zipcode/dl/roman-zip.html"')
    args = vars(parser.parse_args())
    add2zip_list(args)

    import doctest
    doctest.testmod()
