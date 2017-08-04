from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Item, User

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

# Create User
User1 = User(name="Chris", email="email@example.com", picture="example.jpg")
session.add(User1)
session.commit()


# Create dummy user
Item1 = Item(name="Goggles", category="Skiing", description="They protect\
 your eyes from sun and snow", user_id=1)
session.add(Item1)
session.commit()

Item1 = Item(name="Skis", category="Skiing", description="The go on your\
 boots and help you ski", user_id=1)
session.add(Item1)
session.commit()

Item1 = Item(name="Basketball", category="Basketball", description="Big\
 orange ball", user_id=1)
session.add(Item1)
session.commit()

Item1 = Item(name="Net", category="Basketball", description="You shoot the\
 basketball through it", user_id=1)
session.add(Item1)
session.commit()

Item1 = Item(name="Swim Cap", category="Swimming", description="Slows down\
 resistance and makes you glide", user_id=1)
session.add(Item1)
session.commit()

Item1 = Item(name="Goggles", category="Swimming", description="Keeps the\
 water out of your eyes", user_id=1)
session.add(Item1)
session.commit()
