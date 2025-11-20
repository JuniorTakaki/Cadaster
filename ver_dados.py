import sqlite3

con = sqlite3.connect("produto.db")
cur = con.cursor()

# 1) Mostra o esquema da tabela (garante que criou certo)
cur.execute("PRAGMA table_info(produtos)")
print("TABELA produtos (colunas):")
for col in cur.fetchall():
    print(col)  # (cid, name, type, notnull, dflt_value, pk)

print("\nREGISTROS:")
cur.execute("SELECT id, nome, quantidade, ano FROM produtos ORDER BY id")
for row in cur.fetchall():
    print(row)  # (id, nome, quantidade, ano)

con.close()
