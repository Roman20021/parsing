import sqlite3
def data_table(PRISE, DISCOUNT, a):
    counter = 0
    counter1 = 0
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    sql.execute(''' CREATE TABLE IF NOT EXISTS user1010( price_1 TEXT,discount_1 TEXT )''')
    db.commit()
    sql.execute(f"insert into user1010 values('{PRISE}', '{DISCOUNT}')")
    db.commit()
    for value in sql.execute("select * from user1010"):
        counter = counter + 1
        PRISE = int(value[0])
        DISCOUNT = int(value[-1])
    for value1 in sql.execute("select * from user1010"):
        counter1 = counter1 + 1
        if counter1 == counter - 1:
            PRISE_1 = int(value1[0])
    if counter == 1:   
        if DISCOUNT == 0 and PRISE > 0:
            print('цена игры без скидки' + ' ' + '"' + a + '"' + ' ' + 'составляет' + ' ' + str(PRISE) + ' ' + 'руб')
        if DISCOUNT != 0 and PRISE != 0:
            print('цена игры' + ' ' + '"' + a + '"' + ' ' + 'составляет' + ' ' + str(PRISE) + ' ' + 'руб')
            print('скидка составляет' + ' ' + '-' + str(DISCOUNT) + '%') 
        if PRISE == 0:
            print('игра' + ' ' + '"' + a + '"' + ' ' + 'бесплатная')
    if counter != 1:
        if PRISE < PRISE_1:
            print('цена игры' + ' ' + '"' + a + '"' + ' ' + 'снизилась на' + ' ' + str(PRISE_1 - PRISE ) + ' ' + 'руб') 
            exit_the_program = input(' хотите ли вы просматривать цены другой игры:' )
            if exit_the_program == 'да':
                db.execute("delete from user1010 where price_1 >= 0")
                db.commit()
                return exit_the_program
        if PRISE > PRISE_1:
            print('цена игры' + ' ' + '"' + a + '"' + ' ' + 'повысилась на' + ' ' + str(PRISE - PRISE_1  )+ ' ' + 'руб') 
        if PRISE == PRISE_1:
            print("цена не изменилась")
            