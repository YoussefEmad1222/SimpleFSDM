import json
import os
import sys
import unittest  # The test framework
from Schemakeys import Schema_Keys
from create_command import CreateCommand

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
sys.path.append(root_dir)

sys.path.append(root_dir + "/commands")

parent_dir = os.getcwd()
schema = "schema.json"


class Test_Commands(unittest.TestCase):
    def test_wrong_input(self):
        wrong_schema = "schema.json"
        self.assertRaises(Exception, CreateCommand(wrong_schema).execute)

    def test_no_input(self):
        self.assertRaises(Exception, CreateCommand(None).execute)

    def test_create_database(self):
        db_name = "Check-in"
        db_path = parent_dir + "/" + db_name
        self.assertEqual(os.path.exists(db_path), True)

    def test_create_tables(self):
        db_name = "Check-in"
        for table in json.load(open(schema, "r"))[Schema_Keys().TABLES]:
            table_path = parent_dir + "/" + db_name + "/" + table[Schema_Keys().NAME]
            self.assertEqual(os.path.exists(table_path), True)

    def test_wrong_db_name(self):
        db_name = "Check-in"
        table = "Flights_Details"
        t_path = parent_dir + "/" + db_name + "/" + table
        self.assertEqual(os.path.exists(t_path), False)

    def test_create_multiple_time(self):
        db_name = "Check-in"
        db_path = parent_dir + "/" + db_name
        for i in range(3):
            CreateCommand(schema).execute()
            self.assertEqual(os.path.exists(db_path), True)

    def test_set_n_get(self):
        os.system("-c create -sc schema ")
        os.system("-c set -db check-in -t Tables -pk 1.json -v {'Flight_id_seat_no': '01007117106','id':'033788150' }")
        x = os.system("-c set -db check-in -t Tables -pk 1.json")
        ans = {'Flight_id_seat_no': '01007117106', 'id': '033788150'}
        self.assertEqual(x, ans)


if __name__ != '__main__':
    CreateCommand(schema).execute()
    unittest.main()
