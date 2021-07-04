import sqlite3

conn = sqlite3.connect('orgdb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS orgCounts')

cur.execute('CREATE TABLE orgCounts (org TEXT, count INTEGER)')

file_name = input('Enter file name: ')
if len(file_name) < 1: file_name = 'mbox.txt'
fh = open(file_name)

i = 0

for line in fh:
    # i+=1
    # if i % 100 == 0:
    #     conn.commit()
    if not line.startswith('From:'): continue
    pieces = line.split()
    org = pieces[1].split('@')
    org = org[1]
    cur.execute('SELECT count FROM  orgCounts Where org = ? ',(org, ))
    row = cur.fetchone()
    if row is None:
        cur.execute('INSERT INTO orgCounts (org, count) Values (?, 1)', (org, ))
    else:
        cur.execute('UPDATE orgCounts SET count = count + 1 WHERE org = ?', (org, ))
conn.commit()

sqlstr = 'SELECT org, count FROM orgCounts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
