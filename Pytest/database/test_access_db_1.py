"""Update how to access to db with lese codes, create setup_module."""
from access_db import University


conn = None
cur = None

"""
We create setup_module() method to avoid repetion of codes
"""


def setup_module(module):
    global conn
    global cur

    db = University()
    conn = db.access('server')
    cur = conn.cursor()


'''
when the setup_module run which connect to the db we need to run another 
method to close curs and close conn
'''


def teardown_module(module):
    # cur.close()
    conn.close()


def test_dilshad_id():
    id = cur.execute('select id from university_db where name=Dilshad')
    assert id == 814747


def test_rachel_id():
    id = cur.execute('select id from university_db where name=Rachel')
    assert id == 804878
