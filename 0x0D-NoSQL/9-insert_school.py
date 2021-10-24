#!/usr/bin/env python3
"""
"""


def insert_school(mongo_collection, **kwargs):
    """
    """
    collection = mongo_collection
    inserted = collection.insert_one(kwargs).inserted_id
    return inserted
