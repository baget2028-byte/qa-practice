import sqlite3

conn = sqlite3.connect(":memory:")
cur = conn.cursor()
cur.executescript("""
CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT);
CREATE TABLE orders (id INTEGER PRIMARY KEY, user_id INTEGER, amount INTEGER);

INSERT INTO users VALUES (1, 'Влад'), (2, 'Даша'), (3, 'Антон');
INSERT INTO orders VALUES (1, 1, 100), (2, 1, 250), (3, 2, 80);
""")

def q(sql):
    print(sql.strip())
    for row in cur.execute(sql):
        print("  ", row)
    print()

q("SELECT * FROM users")


q("SELECT * FROM orders WHERE amount > 90")

q("SELECT * FROM orders ORDER BY amount DESC")

q("""
SELECT users.name, orders.amount
FROM users
INNER JOIN orders ON users.id = orders.user_id
""")

q("""
SELECT users.name, orders.amount
FROM users
LEFT JOIN orders ON users.id = orders.user_id
""")

q("""
SELECT users.name, orders.amount
FROM users
LEFT JOIN orders ON users.id = orders.user_id
WHERE orders.id IS NULL
""")
