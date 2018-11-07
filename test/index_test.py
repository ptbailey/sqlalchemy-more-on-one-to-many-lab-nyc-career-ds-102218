import unittest, sqlite3
from models import *
from sqlalchemy import create_engine
from queries import *

if bool(session.query(Player).all()) == False:
    exec(open("./seed.py").read())

class TestHasManyBelongsTo(unittest.TestCase):
    # tests to come
    pass
