import unittest, sqlite3, sys
sys.path.insert(0, '..')
from models import NinjaTurtle, SurfPirate, SkiBum, BingoPlayer

connection = sqlite3.connect('../radical.db')
cursor = connection.cursor()


class TestMigrations(unittest.TestCase):

    def test_add_column_to_ninjaturtles_model(self):
        leonardo = NinjaTurtle(name="Leonardo", headband_color="blue")
        self.assertEqual(leonardo.name, 'Leonardo')
        self.assertEqual(leonardo.headband_color, 'blue')

    def test_add_column_to_ninjaturtles_model_table(self):
        cursor.execute("INSERT INTO ninjaturtles (name, headband_color) VALUES ('Leonardo', 'blue');")
        result = (1, 'Leonardo', 'blue')
        self.assertEqual(cursor.execute("SELECT * FROM ninjaturtles;").fetchone(), result)

    def test_create_surf_pirates_model(self):
        laird = SurfPirate(name='Laird Hamilton', largest_wave_surfed=90, seen_great_white=True, date_started_surfing='2018-05-21 10:00:00')
        self.assertEqual(laird.name, 'Laird Hamilton')
        self.assertEqual(laird.largest_wave_surfed, 90)
        self.assertEqual(laird.seen_great_white, True)
        self.assertEqual(laird.date_started_surfing, '2018-05-21 10:00:00')

    def test_create_surf_pirates_table(self):
        cursor.execute("INSERT INTO surf_pirates (name, largest_wave_surfed, seen_great_white, date_started_surfing) VALUES ('Laird Hamilton', 90, 1, '2018-05-21 10:00:00');")
        result = (1, 'Laird Hamilton', 90, 1, '2018-05-21 10:00:00')
        self.assertEqual(cursor.execute("SELECT * FROM surf_pirates;").fetchone(), result)

    def test_create_ski_bums_model(self):
        tigger = SkiBum(name="Tigger Knecht", acl_surgery_yet=False, vertical_skied=10000000, fave_run_description="Corbet's Couloir", days_skied_to_not_skied_ratio=0.93)
        self.assertEqual(tigger.name, 'Tigger Knecht')
        self.assertEqual(tigger.acl_surgery_yet, False)
        self.assertEqual(tigger.vertical_skied, 10000000)
        self.assertEqual(tigger.fave_run_description, 'Corbet\'s Couloir')
        self.assertEqual(tigger.days_skied_to_not_skied_ratio, 0.93)

    def test_create_ski_bums_table(self):
        cursor.execute("INSERT INTO ski_bums (name, acl_surgery_yet, vertical_skied, fave_run_description, days_skied_to_not_skied_ratio) VALUES ('Tigger Knecht', 0, 10000000, 'Corbet''s Couloir', 0.93);")
        result = (1, 'Tigger Knecht', 0, 10000000, "Corbet's Couloir", 0.93)
        self.assertEqual(cursor.execute("SELECT * FROM ski_bums;").fetchone(), result)

    def test_bingo_player_model(self):
        player_one = BingoPlayer(name='Player One')
        self.assertEqual(player_one.name, 'Player One')
