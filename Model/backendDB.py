import sqlite3

DBASE_FILE = 'dbase/printers.db'

def connect():
    conn = sqlite3.connect("dbase/songs.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS inventroy (faculty_id INTEGER PRIMARY KEY AUTOINCREMENT, first TEXT, last TEXT, office TEXT, printer TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS faculty (cartridge_id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, artist TEXT, album TEXT, year INTEGER)")
    conn.commit()
    conn.close()