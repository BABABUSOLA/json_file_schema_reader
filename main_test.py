import os
import unittest
import json


class TestJSONSchema(unittest.TestCase):

    def setUp(self):
        self.input_file = './data/data_1.json'
        self.output_file = './schema/schema_1.json'

        # self.input_file = './data/data_2.json'
        # self.output_file = './schema/schema_2.json'

    def test_schema_generation(self):
        # Test that the output file has been created
        self.assertTrue(os.path.exists(self.output_file))

        # Test that the output file has the correct structure
        with open(self.output_file, 'r') as f:
            schema_data = json.load(f)
        # self.assertIn('message', schema_data)
        self.assertNotIn('attributes', schema_data)

    def test_output_attributes_key(self):
        # Test that attributes within the "attributes" key are excluded
        output_file = './schema/schema_1.json'
        # output_file = './schema/schema_2.json'

        with open(output_file, 'r') as f:
            data = json.load(f)

        def check_keys(data):
            if isinstance(data, dict):
                for key in data:
                    if key == 'attributes':
                        self.assertNotIn(key, data)
                    check_keys(data[key])
            elif isinstance(data, list):
                for item in data:
                    check_keys(item)
        check_keys(data)

    def test_input_attributes_key(self):
        # Test that attributes within the "message" key are excluded
        input_file = './data/data_1.json'
        # input_file = './data/data_2.json'

        with open(input_file, 'r') as f:
            data = json.load(f)

        def check_keys(data):
            if isinstance(data, dict):
                for key in data:
                    if key == 'message':
                        self.assertIn(key, data)
                    check_keys(data[key])
            elif isinstance(data, list):
                for item in data:
                    check_keys(item)
        check_keys(data)
