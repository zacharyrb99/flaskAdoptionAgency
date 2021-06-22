from models import db, Pet
from app import app

db.drop_all()
db.create_all()

Kilo = Pet(name='Kilo', species='Dog', photo_url='https://images.unsplash.com/photo-1587790311640-50b019663f01?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80', age=3)
Reggie = Pet(name='Reggie', species='Dog', photo_url='https://images.unsplash.com/photo-1508948956644-0017e845d797?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=832&q=80', age=14, available=False)
Bowser = Pet(name='Bowser', species='Cat', photo_url='https://images.unsplash.com/photo-1588000152938-fae9cedc61ce?ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTZ8fGNhdHxlbnwwfDJ8MHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60', age=14, notes='Sweet, Calm, Loving')
Onyx = Pet(name='Onyx', species='Cat', photo_url='https://images.unsplash.com/photo-1615903629900-be1d6190c5a3?ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTN8fGNhdHxlbnwwfDJ8MHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60', age=4, notes='FIV positive')
Morty = Pet(name='Morty', species='Cat', age=1)

petlist=[Kilo,Reggie, Bowser, Onyx, Morty]
db.session.add_all(petlist)
db.session.commit()
