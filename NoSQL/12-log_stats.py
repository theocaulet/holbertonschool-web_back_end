#!/usr/bin/env python3
"""Script that provides some stats about Nginx logs stored in MongoDB"""
import pymongo


def log_stats():
    """Returns some stats about Nginx logs stored in MongoDB"""
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client.logs

    print("{} logs".format(db.nginx.count_documents({})))
    print("Methods:")
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        count = db.nginx.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, count))
    status = db.nginx.count_documents({"method": "GET", "path": "/status"})
    print("{} status check".format(status))


if __name__ == "__main__":
    log_stats()
