import sqlite3

conn = sqlite3.connect(":memory:")
cur = conn.cursor()
cur.executescript("""
CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, city TEXT);
CREATE TABLE orders (id INTEGER PRIMARY KEY, user_id INTEGER, amount INTEGER, status TEXT);

INSERT INTO users VALUES
  (1, 'Влад', 'Гродно'), (2, 'Даша', 'Минск'), (3, 'Антон', 'Гродно'),
  (4, 'Мария', 'Брест'), (5, 'Олег', 'Минск');

INSERT INTO orders VALUES
  (1, 1, 100, 'paid'), (2, 1, 250, 'paid'), (3, 2, 80, 'cancelled'),
  (4, 2, 300, 'paid'), (5, 4, 500, 'paid'), (6, 4, 120, 'new'),
  (7, 1, 60, 'cancelled');
""")

def q(sql):
    print(sql.strip())
    for row in cur.execute(sql):
        print("  ", row)
    print()


q("""SELECT status, COUNT(*) FROM orders GROUP BY status;""")
q("""
SELECT users.name, SUM(orders.amount)
FROM users
INNER JOIN orders ON users.id = orders.user_id
WHERE status = 'paid'                  
GROUP BY users.name               
ORDER BY SUM(orders.amount) DESC
""")
q("""SELECT users.name FROM users LEFT JOIN orders ON users.id = orders.user_id WHERE orders.id IS NULL; """)