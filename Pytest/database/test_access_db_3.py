from access_db import University

import pytest

'''
To run and print setting up display on terminal use
pytest -v -rxs --capture=no
'''

"""we use module to run the print one time when is second version will run tweice
use scope equal to module to avoid duplication of printing settingup."""


@pytest.fixture(scope='module')
def cur():
    print('Setting up')
    db = University()
    conn = db.access('server')
    curs = conn.cursor()
    # to run teardown use yield
    yield curs
    conn.close()
    print('\nClosing and disconnect database')


def test_dilshad_id(cur):
    id = cur.execute('select id from university_db where name=Dilshad')
    assert id == 814747


def test_rachel_id(cur):
    id = cur.execute('select id from university_db where name=Rachel')
    assert id == 804878
