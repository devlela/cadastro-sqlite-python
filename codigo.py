import sqlite3

con = sqlite3.connect("usuarios.db")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY, nome TEXT)")
cur.execute("INSERT INTO usuarios (nome) VALUES (?)", ("Wesley",))
con.commit()
for row in cur.execute("SELECT * FROM usuarios"):
    print(row)
con.close()
