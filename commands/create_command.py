import json
import os
import sys
from Schemakeys import Schema_Keys
from Icommand import ICommand

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
sys.path.append(parent_dir)


class CreateCommand(ICommand):
    def __init__(self, schema):
        self.schema = schema
        self.data = json.load(open(schema, "r"))

    def execute(self):
        if self.schema is None or not os.path.exists(os.path.join(parent_dir, self.schema)):
            raise Exception("FileNotFound")

        if not SchemaKeys().DATABASE in self.data:
            raise Exception("DatabaseNameIsMissing")

        dir = self.data[Schema_Keys().DATABASE]
        path = os.path.join(parent_dir, dir)

        os.makedirs(path, exist_ok=True)

        if not Schema_Keys().TABLES in self.data:
            return

        for table in self.data[Schema_Keys().TABLES]:
            t_path = os.path.join(path, table[Schema_Keys().NAME])
            os.makedirs(t_path, exist_ok=True)
