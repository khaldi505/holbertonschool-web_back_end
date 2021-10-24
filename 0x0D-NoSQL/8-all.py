#!/usr/bin/env python3
"""
doc doc pt 0
"""


def list_all(mongo_collection):
    """
    doc doc pt 0
    """
    result = mongo_collection.school.find()
    if result:
        return result
    return []
