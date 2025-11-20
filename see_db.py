import sqlite3

con = sqlite3.connect("register.db")
cur = con.cursor()

# 1) Mostra o esquema da tabela (garante que criou certo)
cur.execute("PRAGMA table_info(register)")
print("TABELA register (col):")
for col in cur.fetchall():
    print(col)  # (cid, name, type, notnull, dflt_value, pk)

print("\nREGISTROS:")
cur.execute("SELECT id, name, surname, year FROM register ORDER BY id")
for row in cur.fetchall():
    print(row)  # (id, name, surname, year)

con.close()
