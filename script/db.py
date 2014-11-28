import os
import sqlite3
path = os.path.join(os.path.join(os.path.dirname(__file__), 'storage'),'app.db')
def init_db():
    if os.path.isfile(dbpath):
        os.remove(dbpath)


def init_app():
    sql = '''CREATE TABLE IF NOT EXISTS app (
name TEXT primary key, 
github_url TEXT, 
description TEXT,
order INTEGER)'''
    db = sqlite3.connect(path)
    db.executescript(sql)
    db.close()

def to_app(data):
    conn = sqlite3.connect(path)
    c = conn.cursor()
    sql = '''CREATE TABLE IF NOT EXISTS app (
name TEXT primary key, 
github TEXT, 
url TEXT, 
description TEXT,
update_time TEXT)'''
    c.execute(sql)
    for d in data:
        d['description'] = d['description'].replace('"', "'")
        if d['url'] is None:
            d['url'] = ''
        sql = '''INSERT INTO app VALUES (
"%s", "%s", "%s", "%s", "%s")''' % (d['name'], d['github'], d['url'], d['description'],d['update'])
        try:
            c.execute(sql)
        except sqlite3.IntegrityError, e:
            sql = '''UPDATE app SET
github="%s",
url="%s",
description="%s",
update_time="%s" where name = "%s"''' % (d['github'], d['url'], d['description'], d['update'], d['name'])
            c.execute(sql)
    conn.commit()
    conn.close()
