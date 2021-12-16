from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from model.user import User

engine = create_engine('postgresql://myadmin:mypw@localhost/demo5')
user1 = User(name='alice', height=177, weight=65)
user2 = User(name='bob', height=166, weight=62)
user3 = User(name='charlie', height=186, weight=86)
with Session(engine) as session:
    session.add(user1)
    session.add(user2)
    session.add(user3)
    session.commit()
