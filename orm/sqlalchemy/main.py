# 'postgres://username:password@localhost/db_name'

from sqlalchemy import create_engine, Column, Integer, String    #
from sqlalchemy.ext.declarative import declarative_base          #
from sqlalchemy.orm import sessionmaker                          #
from pydantic_sqlalchemy import sqlalchemy_to_pydantic           #



DATABASE_URL = 'postgresql://hello:1@localhost/product_items'    #
engine = create_engine(DATABASE_URL)                             #
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) # позволяет бросать запросы

Base = declarative_base() # создает базовый класс

class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    dascription = Column(String)
    price = Column(Integer)
    
ItemPydantic = sqlalchemy_to_pydantic(Item, exclude=['id'])

# API - способ взаимодействиями
# http - протокол 

Base.metadata.create_all(bind=engine)
db_item = ItemPydantic(name= 'item 3', dascription='bag', price=250)

def create_item(db_item:ItemPydantic):
    db_item = Item(**db_item.dict())    
    with SessionLocal() as db:
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
    return db_item

# create_item(db_item)

def get_item():
    result = []
    with SessionLocal() as db:
        items = db.query(Item).all()
        for item in items:
            result.append({'name': item.name,
                           'dascription': item.dascription,
                           'price':item.price})
    return result


print(get_item())

# retrieve - поиск по айди 
# update - 
# delete - принимает айди и удаляет 
# 

"""def retrieve_item(id_):
    with SessionLocal() as db: # открывает бд
        if id_ in db.query(Item).filter_by(id=id_):
            items = db.query(Item).filter_by(id=id_).first()
        else:
            return 'нету такго id'
    return {'name': items.name, 'description': items.dascription, 'price': items.price}
print(retrieve_item(4))    


def update_item(id_, n, d, p):
    with SessionLocal() as db:
        db.query(Item).filter_by(id=id_).update({'name': n, 'dascription': d, 'price': p})
        db.commit()
        items = db.query(Item).filter_by(id=id_).first()
    return {'name': items.name, 'description': items.dascription, 'price': items.price}

print(update_item(2, 'Iphone 15', '2023 year', 120000))


def delete_item(id_):
    with SessionLocal() as db:
        items = db.query(Item).filter_by(id=id_).first()
        if items:
            db.delete(items)
            db.commit()
            return f'значение под ключом {id_} был удален'
        else:
            return f'значение под ключом {id_} не существует'
        
print(delete_item(5))"""

# first - обрабатывает запрос

# def retrieve(id_:int):
#     with SessionLocal() as db:
#         db




def retrieve_item(item_id:int):
    with SessionLocal() as db:
        db_item = db.query(Item).filter(Item.id==item_id).first()

        if db_item is None:
            return None
        return {
            'name':db_item.name,
            'dascription': db_item.dascription,
            'price': db_item.price
        }
print(retrieve_item(4))


def update_item(item_id,item):
    with SessionLocal() as db:
        db_item = db.query(Item).filter(Item.id==item_id).first()
        for field,value in item.items():
            setattr(db_item,field,value)
        db.commit()
        db.refresh(db_item)
        return db_item


def delete_item(item_id):
    with SessionLocal() as db:
        deleted_item = db.query(Item).filter_by(id=item_id).first()
        if deleted_item:
            db.delete(deleted_item)
            db.commit()
            return {'message': f"Item with ID {item_id} deleted successfully"}
        else:
            return {'message': f"Item with ID {item_id} not found"}

    



# REST - {"name":"item 1"}
# SOAP

# client - api - server