#!/usr/bin/env python3
"""Module for updating the topics of a school document in MongoDB."""


def update_topics(mongo_collection, name, topics):
    """Update all documents matching name with the given list of topics."""
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
