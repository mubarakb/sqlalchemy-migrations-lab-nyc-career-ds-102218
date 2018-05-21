from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class NinjaTurtle(Base):
    __tablename__ = 'ninja_turtles'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name, headband_color):
        self.name = name

# Add other classes here


engine = create_engine('sqlite:///radical.db')
Base.metadata.create_all(engine)
