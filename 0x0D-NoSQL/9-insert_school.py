#!/usr/bin/env python3
"""
doc doc placeholder
"""


def insert_school(mongo_collection, **kwargs):
    """
    doc doc
    """
    insertedId = mongo_collection.insert_one(kwargs).inserted_id
    return insertedId
