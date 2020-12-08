import sqlite3
def name():
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    try:
        for value in sql.execute("select * from u802"):    
            NAME = value[0]
            cd = int(value[-1])
    except:
        cd = 0        
    cd = cd + 1    
    sql.execute(''' CREATE TABLE IF NOT EXISTS u802(name ,number )''')
    db.commit()
    if cd == 1:
        sql.execute(f"insert into u802 values('{input('введите название игры с zaka-zaka:').lower()}', '{cd}')")
        db.commit()
        for value in sql.execute("select * from u802"):    
            NAME = value[0]
    return NAME