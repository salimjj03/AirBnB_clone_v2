#!/usr/bin/python3
""" Test delete feature
"""
from models.engine.db_storage import DBStorage
from models.state import State

db = DBStorage()

new = State()
r = db.all(new)

print(r)


