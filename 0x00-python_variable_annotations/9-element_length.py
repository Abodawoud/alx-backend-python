#!/usr/bin/env python3
"""Basic annotations - element length"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Return list of tuples, each tuple is an element and its length """
    return [(i, len(i)) for i in lst]
