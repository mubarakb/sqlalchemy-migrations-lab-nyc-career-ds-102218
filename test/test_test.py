import unittest, sqlite3, sys, datetime
sys.path.insert(0, '..')
from models import NinjaTurtle, SurfPirate, SkiBum, BingoPlayer
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

connection = sqlite3.connect('../radical.db')
cursor = connection.cursor()

engine = create_engine('sqlite:///../radical.db', echo=True)


class TestMigrations(unittest.TestCase):
    Session = sessionmaker(bind=engine)
    session = Session()

    def test_add_column_to_ninjaturtles(self):
        leonardo = NinjaTurtle(name="Leonardo", headband_color="blue")
        self.session.add(leonardo)
        self.session.commit()

        result = (1, 'Leonardo', 'blue')
        self.assertEqual(cursor.execute("SELECT * FROM ninjaturtles;").fetchone(), result)
        self.session.close()

    # def test_create_surf_pirates(self):
    #     test_datetime = datetime.datetime.now()
    #     laird_hamilton = SurfPirate(name="Laird Hamilton", largest_wave_surfed=90, seen_great_white=True, date_started_surfing=test_datetime)
    #
    #     self.session.add(laird_hamilton)
    #     self.session.commit()
    #     import pdb; pdb.set_trace()
    #     cursor.execute("SELECT * FROM surf_pirates;").fetchall()

    def test_create_ski_bums(self):
        tigger = SkiBum(name="tigger knecht", acl_surgery_yet=False, vertical_skied=10000000, fave_run_description="Corbet's Couloir", days_skied_to_not_skied_ratio=0.93)
        self.session.add(tigger)
        self.session.commit()
        import pdb; pdb.set_trace()
