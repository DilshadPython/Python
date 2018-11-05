from access_db import University


def test_dilshad_id():
    db = University()
    conn = db.access('server')
    cur = conn.cursor()
    id = cur.execute('select id from university_db where name=Dilshad')
    assert id == 814747


def test_rachel_id():
    db = University()
    conn = db.access('server')
    cur = conn.cursor()
    id = cur.execute('select id from university_db where name=Rachel')
    assert id == 804878
