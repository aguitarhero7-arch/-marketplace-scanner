import sqlite3
def connect():
 d=sqlite3.connect('marketplace.db'); d.row_factory=sqlite3.Row
 d.execute('CREATE TABLE IF NOT EXISTS listings(id INTEGER PRIMARY KEY,source TEXT,external_id TEXT,title TEXT,price REAL,location TEXT,state TEXT,url TEXT,matches TEXT,first_seen TIMESTAMP DEFAULT CURRENT_TIMESTAMP,UNIQUE(source,external_id))'); d.commit(); return d
def save(d,x,m):
 c=d.execute('INSERT OR IGNORE INTO listings(source,external_id,title,price,location,state,url,matches) VALUES(?,?,?,?,?,?,?,?)',(x.source,x.external_id,x.title,x.price,x.location,x.state,x.url,', '.join(m))); d.commit(); return c.rowcount>0
