# 'postgres://username:password@localhost/db_name'
from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base          
from sqlalchemy.orm import sessionmaker                          
from pydantic_sqlalchemy import sqlalchemy_to_pydantic  
from db_.db_database import * 

# создаем движок SqlAlchemy
engine = create_engine(DATABASE_URL)    
# создаем класс сессии                         
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# создаем модель, объекты которой будут храниться в бд
Base = declarative_base()

# структура для создание таблицы book
class Item(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    author = Column(String)
    genre = Column(String)
    created_at = Column(Date)



# ItemPydantic принимает Item 
ItemPydantic = sqlalchemy_to_pydantic(Item, exclude=['id'])
# создаем таблицы
Base.metadata.create_all(bind=engine)
# создаем объект ItemPydantic для добавления в бд
db_book = ItemPydantic(title='book4', author='Ecenin', genre='t', created_at="1970-12-16")

# добавляем в бд
def create(db_book:ItemPydantic):
    db_item = Item(**db_book.dict())    
    with SessionLocal() as db:
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
    return db_item
# create(db_book)

# получение всех объектов
def read():
    result = []
    with SessionLocal() as db:
        items = db.query(Item).all()
        for item in items:
            result.append({
                'id': item.id,
                'title': item.title,
                'author': item.author,
                'genre': item.genre,
                'created_at': item.created_at
                })
        return result
    

# получение одного объекта по id
def read_one(id_):
    with SessionLocal() as db:
        items = db.query(Item).filter(Item.id==id_).first()

        if items is None:
            return None
        return {
                'title':items.title,
                'author': items.author,
                'genre': items.genre,
                'created_at': items.created_at
            }
# print(read())


# Обновлениепо id
def update(item_id,item:ItemPydantic):
    with SessionLocal() as db:
        db_item = db.query(Item).filter(Item.id==item_id).first()
        for field,value in item.dict().items():
            setattr(db_item,field,value)
        db.commit()
        db.refresh(db_item)
        return db_item


# print(update(2, db_book))


# удаляем объект по id
def delete(item_id):
    with SessionLocal() as db:
        deleted_item = db.query(Item).filter_by(id=item_id).first()
        if deleted_item:
            db.delete(deleted_item)
            db.commit()
            return {'message': f"Item with ID {item_id} deleted successfully"}
        else:
            return {'message': f"Item with ID {item_id} not found"}



# print(delete(1))


