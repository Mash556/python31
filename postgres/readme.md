любая команда в postgresql - заканчивается точка запятой если его не прописать то процес просто будет игнорить эту команду но его можно передать уже в следующей строке

\c - подключение к бд
\du - показывает всех пользователей внутри postgres (users)
\dt - показывает все таблицы внутри бд
\d <название таблицы> - более подробнее информация о таблице
\l - показывает весь список бд
\q - выход из субд(quit)

sudo -u postgres psql - команда для захода через юзера postgres

CREATE USER <название юзера> WITH PASSWORD 'password'; - создает юзера 
ALTER ROLE <username> WITH <привилегии тут какраз пишется те права которого мы хотим присвоить к этому юзеру>; - для обновлении дает какие то права и т.д 
CREATE DATABASE <username> WITH OWNER <username>;

"типы данных"
int:
    bigint - 8 - байтовые числа 
    integer - 4 - байтовые числай
    smallint - 2 - байтовые 
    seria - авто инкрементация 
str:
    char(10) - фиксирование длины строки
    varchar(10) - фиксирование длины строки (не превышает 255 символов)
    text - безграничная длина строки

date:
    timestamp - дата и время
    time - время
    date - дата

boolean - true | false


<!-- char | varchar -->
CREATE DATABASE <название бд>; - создает базу данных 
CREATE TABLE <название таблицы> (
    columb varchar NOT NULL 
); - создает таблицу
INT PRIMARY KEY AUTO_INCREMENT - передается при создании айди чтобы последовательность само сгенерировалось
drop database <название бд> - удаляет бд

primery key 
foreign key 
unique 
not null
null
check(age>18) - чтобы проверять кикие то данные




"""заполнение таблиц"""
синтаксис дополлнение или добавление элемента в таблицу
можно сразу добавлять несколько значении
insert into <название таблицы> (<столбец 1>, <столбец 2>) values (<значение 1>б <значение 2>)
insert into product (name, price) values ('Iphone 14', 24000);
insert into product (name, price) values ('Iphone 13', 24000), ('Iphone 5', 5000), ('Macbook', 74000);
insert into product (name) values ('aaa');

### вывод данных из таблицы
select * from <название таблицы>;

показывает элемент который есть внутри таблицы product
select * from product;

### условие 
ORDER BY - сортирует данные по убыванию или возрастанию
ASC(по возрастанию)
DESC(по убыванию)

select * from product ORDER BY price;
select * from product ORDER BY id;
select * from product ORDER BY price DESC;

LIMIT - возвращает аграниченное количество данных

select * from <название таблицы> order by price limit <лимит количество>;

select * from product order by price limit 3;

select * from product order by price offset 5; пропускает первые 5 записей

DISTINCT - убирает дубликаты и возвращает только уникальные значение 
select DISTINCT price from product;


WHERE - фильтрация по каким то критериям  
<!-- >, <, >=, <=, !=, = -->
or 
and
not 
in


BETWEEN - диапозон
select * from product where price BETWEEN 16000 and 24000;

LIKE - выводит результат который подходит введенному шаблону он чувствителен к регистру
where name like 'A%' - имена нач на букву А
where name like '%gmail.com' - имеил заканчивающий указанный нами шаблином
ILIKE - выводит результат который подходит введенному шаблону он не чувствителен к регистру
select * from product where name ILIKE 'iphone%';


### Удаление записей из таблиц
delete from product


UPDATE <название таблицы> SET name = 'Iphone 18' 

# AS
select name , price *89 as dollars  from product;

# GROUP BY  - это ключевое слово которое позволяет выводить значение из колонок обьединенные в группы
select name, sum(price) from product group by name;

# HAVING - точно такое же условие как WHERE но всегда используется с GROUP BY, выводит результат условия для групп
select name, sum(price) from product where price < 24000 group by name having name = 'Iphone 5';

# WHERE - выводит результат условия для строк 



##### СВЯЗИ
One to One - связь один к одному
один человек один ID
один человек один мозг
одна страна один флаг

One to Many - один ко многим
одна книга - много страниц
один куратор - много студентов
один автор - много книг

Many to Many - многие ко многим
много аккаунтов гит - много репозиториев
много предметов - много учеников
много машин - много запчастей

PRIMARY KEY - внешний ключ (с помощью него создаются связи)

FOREIGN KEY - первичный ключ (он ссылается на  PRIMARY KEY)

# one to one - к id другой таблицы даем уникальность 
create table author (
id serial PRIMARY KEY,
name varchar(50) not null);

create table book(
id serial primary key,
title varchar(40) not null,
create_at date,
author_id int,
CONSTRAINT fk_book_author
foreign key (author_id) references author (id));


# one to many - ссылаемся на id другой таблицы
create table country(
id serial primary key,
language varchar(10) not null,
capital varchar(20) not null);

create table flag(
id serial primary key,
created_at date not null,
country_id int unique,
constraint fk_flag_country
foreign key (country_id) references country (id));

# many to many - создаем третью таблицу в которой ссылается на две связные  
create table student(
id serial primary key,
name varchar(50) not null,
age int check(age>0));

create table subject(
id serial primary key,
title varchar(30) not null,
teacher varchar(50) not null);

create table stu_sub(
student_id int,
subject_id int, 
constraint fk_stu foreign key(student_id) references student(id),
constraint fk_sub foreign key(subject_id) references subject(id));



### индексы
Индексы - спец объекты предназначенные в основном для ускорение доступа данным

           32 - 
       12      31  

типы индексов v postgres
1) b - дерево - balanced tree
2) хеш - 
3) gist
4) sp-gist
5) gin
6) brin

create index book_title on book (title);
drop index


### join
join - инструкция которая позволяет в запросах SELECT брать данные из нескольких таблиц 

INNER JOIN (JOIN) - достает только те  записи у которых есть связь
LEFT JOIN - он достает все записи с левой таблицы и с правой таблицы и соединяет с правой таблицей
RIGHT JOIN - то же самое что и LEFT, только отзеркаленный 
FULL JOIN - достает все записи с обеих таблиц 

SELF JOIN 

#### import / export database 
 psql -U <username> -d <название бд> -f <название файла>
 psql -U hello -d shop_db -f file.sql
 <название бд> должна существовать в postgresql

 pg_dump <название бд> > <путь и наз файла>
 pg_dump -U <username> <название бд> > <путь к файлу>


### агрегатные функции
MIN
MAX
 shop_db=# select customer.name, sum(products.price) as total_price from customer join orders on customer.id = orders.customer_id join 
 products on products.id = orders.products_id
 group by customer.name;
    name    | total_price 
 -----------+-------------
  customer2 |         470
  customer1 |        1073
  customer3 |         680
 (3 rows)


COUNT - считает количество записей в сгруппированном поле








##### таски
task 4
Найдите среднее количество параграфов в произведениях жанра t (таблица work).
select avg(totalparagraphs) from work where genretype = 't' 

# BETWEEN - промежуток
task 9
select charname, speechcount from character where speechcount between 15 and 30
#
task 10
select title, year from work where year between 1601 and 1700 


# like - проверяет вхождение переданного элемента чувствителен к регистру
task 11


# distinct - убирает все повторяющиеся значения и возвращает уникальный вид элементов
task 12
select distinct(section) from paragraph;

task 14
select paragraphnum, character.charname, character.speechcount from paragraph join character on paragraph.charid = character.charid;

task 15


task 5
select title from work where totalwords > (select avg(totalwords) from work)





create table customer(
id serial primary key,
name varchar(50));

create table products(
id serial primary key,
title varchar(50),
price int);

create table orders(
id serial primary key,
customer_id int,
products_id int,
constraint order_customer foreign key (customer_id) references customer(id), 
constraint order_products foreign key (products_id) references products(id));

insert into customer (name) values ('customer1'), ('customer2'), ('customer3');

insert into products (title, price) values
('product1', 340),
('product2', 503),
('product3', 470),
('product4', 230),
('product5', 450);

insert into orders (customer_id, products_id) values
(1,1), (1,2), (1,4),
(2,3),
(3,5), (3,4);