#!/usr/bin/env python3
""" 9-insert_school """


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new school into the collection
    Args:        mongo_collection: pymongo collection object
    Returns:     The ID of the inserted document
    """
    return mongo_collection.insert_one(kwargs).inserted_id
