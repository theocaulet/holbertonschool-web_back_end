#!/usr/bin/env python3
""" 8-all """


def list_all(mongo_collection):
    """Lists all documents in the collection
    Args:        mongo_collection: pymongo collection object
    Returns:     list of documents in the collection
    """
    return list(mongo_collection.find())
