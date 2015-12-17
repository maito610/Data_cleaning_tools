#! /usr/bin/env python
#  -*- coding: utf-8 -*-
__author__ = 'maito'
__all__ = ['add2zip_list']

##########
import sys
import argparse
import codecs
import csv

##########
class Add2zip(object):
    """
    [CLASSES] Class説明文
    """

    def parse_address(address):
        return([])

    def add_csv2list(address_list_file):
        address_list = []
        ff = codecs.open(address_list_file,'r','utf-8')
        reader = csv.reader(ff)
        for rr in reader:
            address_list.append(rr)
        return(address_list)

    def zip_csv2dict(zipcode_list_file):
        zipcode_list = []
        ff = codecs.open(zipcode_list_file,'r','shift-jis')
        reader = csv.reader(ff)
        for rr in reader:
            zipcode_list.append(rr)
        return(zipcode_list)

    def add2zip_zipcode(address, zipcode_dict):
        """
        [CLASSES] 関数説明文
        Keyword arguments:
        hoge -- 引数説明
        """
        # >>> add2zip_list(args)
        pass


def main():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument(
        '-a',
        dest = 'address_list_file',
        nargs='?',
        default='../data/address.csv',
        help='address to get zip code')
    parser.add_argument(
        '-f',
        dest = 'zipcode_list_file',
        nargs='?',
        default='../data/KEN_ALL.CSV',
        help='file path of postal zip code list KEN_ALL.CSV "http://www.post.japanpost.jp/zipcode/dl/kogaki/zip/ken_all.zip"')
    args = vars(parser.parse_args())

    address_list = Add2zip.add_csv2list(args['address_list_file'])
    zipcode_dict = Add2zip.zip_csv2dict(args['zipcode_list_file'])

    print(address_list[0])
    print(zipcode_dict[0])

    Add2zip.add2zip_zipcode('1',{})


##########
if __name__ == '__main__':
    main()
    # >>> Add2zip.parse_address('東京都港区芝浦4-4-27-501')

    import doctest
    doctest.testmod()
