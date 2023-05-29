from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Create the SQLAlchemy engine and session
engine = create_engine('your_database_connection_string')
Session = sessionmaker(bind=engine)
session = Session()

# Create the base model class
Base = declarative_base()

# Define the table models
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    posts = relationship('Post', back_populates='user')

class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='posts')

class Comment(Base):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True)
    content = Column(String)
    post_id = Column(Integer, ForeignKey('posts.id'))
    post = relationship('Post', back_populates='comments')

# Joining the tables
query = session.query(User).join(User.posts).join(Post.comments)

# Retrieve the results
results = query.all()

# Print the results
for user in results:
    print('User:', user.name)
    for post in user.posts:
        print('  Post:', post.title)
        for comment in post.comments:
            print('    Comment:', comment.content)
