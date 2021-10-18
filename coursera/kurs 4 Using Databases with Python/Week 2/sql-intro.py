import sqlite3

conn = sqlite3.connect('Ages.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Ages')

cur.execute('CREATE TABLE Ages(name VARCHAR(128), age INTEGER)')

str = '''DELETE FROM Ages;INSERT INTO Ages (name, age) VALUES ('Coray', 18);INSERT INTO Ages (name, age) VALUES ('Tanzina', 23);INSERT INTO Ages (name, age) VALUES ('Gjan', 28);INSERT INTO Ages (name, age) VALUES ('Alexanne', 16);INSERT INTO Ages (name, age) VALUES ('Hajra', 16);INSERT INTO Ages (name, age) VALUES ('Karen', 25);'''
lst = str.split(";")
for i in range(len(lst)):
    cur.execute(lst[i])
    print(lst[i])


conn.commit()
