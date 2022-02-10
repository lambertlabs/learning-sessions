from typing import List

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from autosqla import User, Document

engine = create_engine('postgresql://postgres:Nader1739@localhost/mydb')
session_maker = sessionmaker(bind=engine)
db: Session = session_maker()

db.query(Document).delete()
db.query(User).delete()
db.commit()

n: int = 3
for i in range(n):
    new_user = User(
        username=f"John Smith {i}",
        email="john@gmail.com"
    )
    db.add(new_user)
db.commit()

all_users: List[User] = db.query(User).all()
print([user.username for user in all_users])

for i in range(n):
    new_document = Document(
        title=f"Document {i}",
        contents="Once upon a time...",
        user=all_users[i]
    )
    db.add(new_document)
db.commit()

all_documents: List[Document] = db.query(Document).all()
print([document.title for document in all_documents])
