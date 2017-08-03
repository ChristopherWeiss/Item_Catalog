from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import  Base, Item

engine = create_engine('sqlite:///itemcatalogwithusers.db') 
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create dummy user
User1 = User(name="Goggles", category="Skiing", description = "They protect your eyes from sun and snow")
session.add(Item1)
session.commit()

User1 = User(name="Skis", category="Skiing", description = "The go on your boots and help you ski")
session.add(Item1)
session.commit()

User1 = User(name="Basketball", category="Basketball", description = "Big orange ball")
session.add(Item1)
session.commit()

User1 = User(name="Net", category="Basketball", description = "You shoot the basketball through it")
session.add(Item1)
session.commit()

User1 = User(name="Swim Cap", category="Swimming", description = "Slows down resistance and makes you glide")
session.add(Item1)
session.commit()

User1 = User(name="Goggles", category="Swimming", description = "Keeps the water out of your eyes")
session.add(Item1)
session.commit()