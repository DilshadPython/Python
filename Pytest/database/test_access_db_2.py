from access_db import University

import pytest

'''
To run and print setting up display on terminal use
pytest -v -rxs --capture=no
'''


@pytest.fixture()
def cur():
    print('Setting up')
    db = University()
    conn = db.access('server')
    curs = conn.cursor()
    return curs


def test_dilshad_id(cur):
    id = cur.execute('select id from university_db where name=Dilshad')
    assert id == 814747


def test_rachel_id(cur):
    id = cur.execute('select id from university_db where name=Rachel')
    assert id == 804878
