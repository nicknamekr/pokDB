import pokdb
db = pokdb.db('dbcode') # 'dbcode' is database code. you can put any string in this arg.

db.write('a', 'b') # A is B

print(db.get('a'))