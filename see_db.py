import sqlite3

con = sqlite3.connect("database.db")
cur = con.cursor()

# 1) Mostra o esquema da tabela (garante que criou certo)
cur.execute("PRAGMA table_info(register)")
print("TABELA register (col):")
for col in cur.fetchall():
    print(col)  # (cid, name, type, notnull, dflt_value, pk)

print("\nREGISTROS:")
cur.execute("SELECT id, name, surname, year FROM users ORDER BY id ")
# cur.execute("SELECT id, brand, model, car_year, car_color FROM cars ORDER BY id")
for row in cur.fetchall():
    print(row)  # (id, name, surname, year)

con.close()
