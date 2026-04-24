#!/usr/bin/env python3
"""Module for inserting a document into a MongoDB collection."""


def insert_school(mongo_collection, **kwargs):
    """Insert a new document built from kwargs and return its new _id."""
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
