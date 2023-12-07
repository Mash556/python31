# orm - это технология позволяющая автоматически связать бд с кодом

# psycapg2 - это библиотека, которое предостовляет интерфейс питон для взаимодействия с Postgresql

import psycopg2

db_params = {
    'host':'localhost',
    'database':'practice_psyco',
    'user': 'hello',
    'password':'1'
}

connection = psycopg2.connect(**db_params)

create_table = """
CREATE TABLE test (
id serial primary key,
name varchar(30),
age integer);
"""

data = [
    ('Nikita', 20),
    ('Nikita', 20),
    ('Nikita', 20),
    ('Nikita', 20)
]
insert_query = f"""
insert into test (name, age) values {data}
"""
insert_query = """
insert into test (name, age) values (%s, %s);
"""

select_query = """
select * from test;
"""
update_query = """
update test set name = %s where id = %s
"""
# data  = ('SHERLACK', 5)
a = 1
delete_query = f"""
delete from test where id = {a}
"""


try:
    cursor = connection.cursor()
    # cursor.execute(select_query)
    cursor.executemany(insert_query, data) # выполнение sql
    connection.commit()
    # result = cursor.fetchall() # это функция выводит данные пишем когда мы ожидаем данные
    # print(result)
finally:
    cursor.close()
    connection.close()


# peewee
# sqllalchemy