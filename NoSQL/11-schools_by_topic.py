#!/usr/bin/env python3
"""Module for finding schools that teach a specific topic in MongoDB."""


def schools_by_topic(mongo_collection, topic):
    """Return a list of schools that have the given topic in their topics list."""
    return list(mongo_collection.find({"topics": topic}))
