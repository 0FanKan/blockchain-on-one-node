import psycopg2
from block import Block

connect = psycopg2.connect("dbname=BChain user=sensei")
connect.autocommit = True
cur = connect.cursor()

cur.execute("DROP TABLE chain")
cur.execute("""CREATE TABLE chain (
            index serial PRIMARY KEY,
            timestamp timestamp,
            prev_hash text,
            hash text,
            data text,
            nonce integer
        )""")

cur.execute(
    "INSERT INTO chain (index, prev_hash, hash, data) VALUES (%s, %s, %s, %s)",
    (1, 12345, 678910, "Hello"))

cur.execute(
    "INSERT INTO chain (index, prev_hash, hash, data) VALUES (%s, %s, %s, %s)",
    (2, 12345, 678910, "Hello"))

node = []
cur.execute("SELECT * FROM chain")

for i in cur:
    block = {
        "index": i[0],
        "timestamp": i[1],
        "data": i[2],
        "prev_hash": i[3],
        "hash": i[4],
        "Nonce": i[5]
    }
    node.append(Block(block))

print(node)