#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Module for simplifying interactions with github
'''
import sys

def main(args):
    '''
    '''
    return 0


if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser(decription=main.__doc__)
    args = parser.parse_args()
    sys.exit(main(args))
