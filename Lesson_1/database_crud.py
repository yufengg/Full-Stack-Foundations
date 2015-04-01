## this is my notes on the lesson

sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

def run_insert():
  print session.query(Restaurant).all()
  myFirstRestaurant = Restaurant(name = 'Pizza Palace')
  session.add(myFirstRestaurant)

  cheesepizza = MenuItem(name = 'Cheese Pizza', description = 'Made with ingredients', course = 'Entree', price = '$8.99', restaurant = myFirstRestaurant)
  session.add(cheesepizza)

  print session.query(Restaurant).all()
  print session.query(MenuItem).all()
  session.commit()

def run_read():
  items = session.query(Restaurant).all()
  for item in items:
    print item.id, item.name

  print '============'

  items = session.query(MenuItem).all()
  for item in items:
    print item.id, item.course, item.name, item.price

def run_update():
  pizzas = session.query(MenuItem).filter_by(name = 'Cheese Pizza')
  for pizza in pizzas:
    print pizza.name, pizza.price

  cheesepizza = session.query(MenuItem).filter_by(id = 1).one()
  print cheesepizza.name, cheesepizza.price
  cheesepizza.price = '$2.99'
  session.add(cheesepizza)
  session.commit()
  cheesepizza = session.query(MenuItem).filter_by(id = 1).one()
  print 'After update: ', cheesepizza.name, cheesepizza.price

def run_delete():
  cheesepizza = session.query(MenuItem).filter_by(id = 1).one()
  print cheesepizza.name, cheesepizza.price
  session.delete(cheesepizza)
  session.commit()
  cheesepizza = session.query(MenuItem).filter_by(id = 1).one()


if __name__ == '__main__':
  run_insert(); print '>>====='
  run_read(); print '>>====='
  run_update(); print '>>====='
  run_delete(); print '>>====='
