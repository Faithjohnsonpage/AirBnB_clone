import unittest
from models.base_model import BaseModel
import datetime
import os


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.my_model = BaseModel()
        self.my_model.name = "My First Model"
        self.my_model.my_number = 89

    def tearDown(self):
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_init_valid_values(self):
        self.assertIsInstance(self.my_model, BaseModel)
        self.assertEqual(self.my_model.name, "My First Model")
        self.assertEqual(self.my_model.my_number, 89)
        self.assertIsNotNone(self.my_model.id)
        self.assertIsInstance(self.my_model.created_at, datetime.datetime)
        self.assertIsInstance(self.my_model.updated_at, datetime.datetime)

    def test_str_representation(self):
        print_value = f"[{type(self.my_model).__name__}] "\
                      f"({self.my_model.id}) {self.my_model.__dict__}"
        self.assertEqual(str(self.my_model), print_value)

    def test_save(self):
        updated_value = self.my_model.updated_at
        self.my_model.save()
        self.assertNotEqual(self.my_model.updated_at, updated_value)

    def test_to_dict(self):
        self.my_model_json = self.my_model.to_dict()
        self.my_model_json = self.my_model.to_dict()
        for key, value in self.my_model_json.items():
            if key == '__class__':
                self.assertEqual(type(value), str)
            else:
                self.assertTrue(type(value) in [int, str])


if __name__ == '__main__':
    unittest.main()
