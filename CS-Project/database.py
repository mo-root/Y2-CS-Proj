from model import *
# import sqlite
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# from IPython.core import get_ipython

# hist = get_ipython().history_manager
# hist.db = sqlite3.connect(hist.hist_file , check_same_thread = False)



engine = create_engine('sqlite:///database.db?check_same_thread=False')
Base.metadata.create_all(engine)
# session = scoped_session(sessionmaker(bind=engine))
DBSession = sessionmaker(bind=engine)
session = DBSession()


def add_place(place,description,date,link):
	place_obj = Place(
		name_of_place = place,
		description=description,
		date_of_visit = date,
		imglink = link)
	session.add(place_obj)
	session.commit()

def query_all():
	Places = session.query(Place).all()
	return Places
