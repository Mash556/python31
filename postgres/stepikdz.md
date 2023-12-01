отношение == таблица
размерность == количество столбца
атрибут == название ряда(поле)
мощбность == число записей(кол-во записей)
кортеж == запись записанный в одну строку


# синтаксис создание таблицы
CREATE TABLE book(название таблицы) (book_id(название поле он обызательный) INT PRIMARY KEY AUTO_INCREMENT(описание характеристики для данного поле), title VARCHAR(50), author VARCHAR(30), price DECIMAL(8, 2), amount INT);



# перед ввыводом данных из таблиц им можно задать новое название поле и даже провести некие операции
select title, amount, amount*1.65 as pack from book;

================ математические функции
#  	возвращает наименьшее целое число, большее или равное x(округляет до целого числа в большую сторону)
CEILING(4.2)=5
CEILING(-5.8)=-5

#  	округляет значение x до k знаков после запятой, если k не указано – x округляется до целого
ROUND(4.361)=4
ROUND(5.86592,1)=5.9

# возвращает наибольшее целое число, меньшее или равное x (округляет до  целого числа в меньшую сторону)
FLOOR(4.2)=4
FLOOR(-5.8)=-6

# возведение x в степень y
POWER(3,4)=81.0

#  	квадратный корень из x
SQRT(4)=2.0
SQRT(2)=1.41...

#  	конвертирует значение x из радиан в градусы
DEGREES(3) = 171.8...

# конвертирует значение x из градусов в радианы
RADIANS(180)=3.14...

# модуль числа x 
ABS(-1) = 1
ABS(1) = 1

# задали новую цену формула для уменьшение в процентах
SELECT title, 
    author, 
    amount,
    ROUND(price-(price*0.3),2) AS new_price
FROM book;



# условие if можно передавать вложенный условие
# в нутри скобки все три параметра необходимы
# синтаксис условие сперва идет ключевое слово if(логическое услоие, результат который будет выполнен если условие верно, будет выполнен если условие не верно)
# формула увеличение числа на какойто процент
select author, title, round(if(author = 'Булгаков М.А.', price+price*0.1, if(author = 'Есенин С.А.', price+price*0.05, price)), 2) as new_price from book;



# where - служит для фильтрации по данному условию
select author, title, price from book where amount < 10;
# where - он содержит в себе знаки сравнение и такие операторы как and, or, not
select title, author, price, amount from book where price<500 and price>600 or price*amount>=5000;

select round(avg(price), 2) as Средняя_цена, 
             round(sum(price*amount),2) as Стоимость 
from book
where amount between 5 and 14;

# оператор BETWEEN(промежуток) и IN(похож на оператора равенства)
select title, author from book where price between 540.50 and 800 and amount in (2,3,5,7);
select author, title from book where amount between 2 and 14 order by author desc, title;

# ORDER BY (сортирует по алфавиту и чисел по умолчанию он сортирует по возрастанию можно предать ещё один параметр после название столбца как DESC(сортирует по убыванию), ASC(сортирует по возрастанию))


# LIKE - проверяет на вхождение он чувствителен к регистру
# 
select title, author from book 
    where title like '_% _%'
    (проверяет состоит ли столбец только из двух слов и разделены ли они пробелом и без знаков препинание)  
    and(открываем новую строку и пошла проверка на другие столбцы) 
    (author like '%С._.' or(после ор идет ещё одна проверка) author like '%_.С.') 
    order by title;(все сортируем)


# DISTINCT - после себя в не скобках передает название столбца и результат будет уникальные элементы этого столбца
select distinct amount from book;
select distinct min(price) as Минимальная_цена , max(price) as Максимальная_цена, round(avg(price), 2) as Средняя_цена 
from book 


# GROUP BY - объединяет в одну группу
select author as Автор, count(title) as Различных_книг, sum(amount) as Количество_экземпляров from book
group by author;


# MIN( выводит минимальное значение), MAX(выводит максимальное значение), AVG(среднее значение)
select author, min(price) as Минимальная_цена, max(price) as Максимальная_цена, avg(price) as Средняя_цена 
from book group by author
# 
select author, sum(price*amount) as Стоимость, 
round(sum(price*amount)*(18/100)/(1+18/100), 2) as НДС,
round(sum(price*amount)/(1+18/100), 2) as Стоимость_без_НДС from
book group by author



# Важно! Порядок ВЫПОЛНЕНИЯ запросов

    FROM
    WHERE
    GROUP BY
    HAVING
    SELECT
    ORDER BY

# HAVING - оно используется только при использовании GROUP BY и всегда стоит после него
select author, sum(price*amount) as Стоимость
from book
where not title in('Идиот', 'Белая гвардия')
group by author 
having Стоимость > 5000
order by Стоимость desc;


# вложенные запросы 
select author, title, price 
from book
where price <= (
    select avg(price)
    from book)
order by price desc;
