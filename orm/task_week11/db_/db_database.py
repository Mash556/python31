import psycopg2
 
conn = psycopg2.connect(dbname="hello", user="hello", password="1", host="localhost")
cursor = conn.cursor()
 
conn.autocommit = True
# команда для создания базы данных metanit
sql = "CREATE DATABASE task"
 
# выполняем код sql
cursor.execute(sql)
print("База данных успешно создана")
 
cursor.close()
conn.close()

# строка подключения
DATABASE_URL = 'postgresql://hello:1@localhost/task'    
