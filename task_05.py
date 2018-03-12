#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Mutability-differences between strings and tuples"""


def flip_keys(to_flip):
    print to_flip
    external_index = 0
    for external_index in range(len(to_flip)):
        internal_list = to_flip[external_index]
        to_flip[external_index]=internal_list[::-1]
        external_index = + 1
    print to_flip
   
    
