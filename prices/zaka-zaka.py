import sqlite3
import name
import data_table
from Discount import Discount
a = name.name()
b = a.replace(' ', '-')
b = b.replace(':', '-')
b = b.replace('--', '-')
b = b.replace('--', '-') 

c = Discount('https://zaka-zaka.com/game/' + b)
try:
    title_free = c.parse_free()
    title_free = 0    #игра бесплатная
except(IndexError):
    title_free = -10  #игра платная
try:   
    title_discount = c.parse_discount() #размер скидки
except(IndexError):
    title_discount = 0   # игра без скидки или игра бесплатная
if title_free == 0:
    p = title_free
    discount = 0
if title_free == -10 and title_discount == 0:
    p = c.parse()
    discount = 0
if title_discount != 0:
    discount = title_discount
    p = c.parse()    
exit_the_program = data_table.data_table(p, discount, a)
if  exit_the_program == 'да':
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    sql.execute(f"insert into u802 values('{0}', '{0}')")
    db.commit()  
