from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class NinjaTurtle(Base):
    __tablename__ = 'ninjaturtles'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    headband_color = Column(String)

    def __init__(self, name, headband_color):
        self.name = name
        self.headband_color = headband_color

class SurfPirate(Base):
    __tablename__ = 'surf_pirates'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    largest_wave_surfed = Column(Integer)
    seen_great_white = Column(Boolean)
    date_started_surfing = Column(DateTime)

    def __init__(self, name, largest_wave_surfed, seen_great_white, date_started_surfing):
        self.name = name
        self.largest_wave_surfed = largest_wave_surfed
        self.seen_great_white = seen_great_white
        self.date_started_surfing = date_started_surfing

class SkiBum(Base):
    __tablename__ = 'ski_bums'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    acl_surgery_yet = Column(Boolean)
    vertical_skied = Column(BigInteger)
    fave_run_description = Column(Text)
    days_skied_to_not_skied_ratio = Column(Float)

    def init(self, name, acl_surgery_yet, vertical_skied, fave_run_description, days_skied_to_not_skied_ratio):
        self.name = name
        self.acl_surgery_yet = acl_surgery_yet
        self.vertical_skied = vertical_skied
        self.fave_run_description = fave_run_description
        self.days_skied_to_not_skied_ratio = days_skied_to_not_skied_ratio

class BingoPlayer(Base):
    __tablename__ = 'bingo_players'
    id = Column(Integer, primary_key=True)
    name = Column(String)


engine = create_engine('sqlite:///radical.db')
Base.metadata.create_all(engine)
