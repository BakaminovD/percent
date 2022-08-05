import sqlite3

def add_new_unit(name, adress):
    value = (name, adress)
    conn = sqlite3.connect('units.db')
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS units(
                    usid INTEGER PRIMARY KEY,
                    usname TEXT,
                    usadress TEXT);
                """)
    conn.commit()
    cur.execute("INSERT INTO units (usname, usadress) VALUES(?, ?);", value)
    conn.commit()
    
def all_units():
    conn = sqlite3.connect('units.db')
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS units(
                    usid INTEGER PRIMARY KEY,
                    usname TEXT,
                    usadress TEXT);
                """)
    conn.commit()
    cur.execute("SELECT * FROM units;")
    all_results = cur.fetchall()
    return all_results

def delit_us(primari_key):
    conn = sqlite3.connect('units.db')
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS units(
                    usid INTEGER PRIMARY KEY,
                    usname TEXT,
                    usadress TEXT);
                """)
    conn.commit()
    cur.execute("DELETE FROM units WHERE usid = ?;", (primari_key,))
    conn.commit()