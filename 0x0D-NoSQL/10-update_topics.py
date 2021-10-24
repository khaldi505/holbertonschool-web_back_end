#!/usr/bin/env python3
"""
doc doc pt 2
"""


def update_topics(mongo_collection, name, topics):
    """
    doc doc pt2
    """
    result = mongo_collection.update_many(
        {"name": name}, {'$set': {'topics': topics}})
    return result
