#!/usr/bin/python3
"""IT Defines unittests for models/user.py.

Unittest classes:
    TestUser_instantiation
    TestUser_save
    TestUser_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.user import User


class TestUserInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the User class."""

    def test_no_args_instantiates(self):
        user = User()
        self.assertEqual(User, type(user))

    def test_new_instance_stored_in_objects(self):
        user = User()
        self.assertIn(user, storage.all().values())

    def test_id_is_public_str(self):
        user = User()
        self.assertEqual(str, type(user.id))

    def test_created_at_is_public_datetime(self):
        user = User()
        self.assertEqual(datetime, type(user.created_at))

    def test_updated_at_is_public_datetime(self):
        user = User()
        self.assertEqual(datetime, type(user.updated_at))

    def test_email_is_public_str(self):
        user = User()
        self.assertEqual(str, type(user.email))

    def test_password_is_public_str(self):
        user = User()
        self.assertEqual(str, type(user.password))

    def test_first_name_is_public_str(self):
        user = User()
        self.assertEqual(str, type(user.first_name))

    def test_last_name_is_public_str(self):
        user = User()
        self.assertEqual(str, type(user.last_name))

    def test_two_users_unique_ids(self):
        user1 = User()
        user2 = User()
        self.assertNotEqual(user1.id, user2.id)

    def test_two_users_different_created_at(self):
        user1 = User()
        sleep(0.05)
        user2 = User()
        self.assertLess(user1.created_at, user2.created_at)

    def test_two_users_different_updated_at(self):
        user1 = User()
        sleep(0.05)
        user2 = User()
        self.assertLess(user1.updated_at, user2.updated_at)

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        user = User()
        user.id = "123456"
        user.created_at = user.updated_at = dt
        user_str = user.__str__()
        self.assertIn("[User] (123456)", user_str)
        self.assertIn("'id': '123456'", user_str)
        self.assertIn("'created_at': " + dt_repr, user_str)
        self.assertIn("'updated_at': " + dt_repr, user_str)

    def test_args_unused(self):
        user = User(None)
        self.assertNotIn(None, user.__dict__.values())

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        user = User(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(user.id, "345")
        self.assertEqual(user.created_at, dt)
        self.assertEqual(user.updated_at, dt)

    def test_instantiation_with_None_kwargs_raises_error(self):
        with self.assertRaises(TypeError):
            User(id=None, created_at=None, updated_at=None)


class TestUser_save(unittest.TestCase):
    """Unittests for testing save method of the User class."""

    @classmethod
    def setUpClass(cls):
        try:
            os.rename("file.json", "tmp")
        except FileNotFoundError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        try:
            os.rename("tmp", "file.json")
        except FileNotFoundError:
            pass

    def test_one_save(self):
        user = User()
        sleep(0.05)
        first_updated_at = user.updated_at
        user.save()
        self.assertLess(first_updated_at, user.updated_at)

    def test_two_saves(self):
        user = User()
        sleep(0.05)
        first_updated_at = user.updated_at
        user.save()
        second_updated_at = user.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        user.save()
        self.assertLess(second_updated_at, user.updated_at)

    def test_save_with_arg_raises_error(self):
        user = User()
        with self.assertRaises(TypeError):
            user.save(None)

    def test_save_updates_file(self):
        user = User()
        user.save()
        user_id = "User." + user.id
        with open("file.json", "r") as f:
            self.assertIn(user_id, f.read())


class TestUser_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the User class."""

    def test_to_dict_type(self):
        user = User()
        self.assertTrue(dict, type(user.to_dict()))

    def test_to_dict_contains_correct_keys(self):
        user = User()
        self.assertIn("id", user.to_dict())
        self.assertIn("created_at", user.to_dict())
        self.assertIn("updated_at", user.to_dict())
        self.assertIn("__class__", user.to_dict())

    def test_to_dict_contains_added_attributes(self):
        user = User()
        user.middle_name = "Holberton"
        user.my_number = 98
        self.assertEqual("Holberton", user.middle_name)
        self.assertIn("my_number", user.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        user = User()
        user_dict = user.to_dict()
        self.assertEqual(str, type(user_dict["id"]))
        self.assertEqual(str, type(user_dict["created_at"]))
        self.assertEqual(str, type(user_dict["updated_at"]))

    def test_to_dict_output(self):
        dt = datetime.today()
        user = User()
        user.id = "123456"
        user.created_at = user.updated_at = dt
        expected_dict = {
            'id': '123456',
            '__class__': 'User',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(user.to_dict(), expected_dict)

    def test_contrast_to_dict_dunder_dict(self):
        user = User()
        self.assertNotEqual(user.to_dict(), user.__dict__)

    def test_to_dict_with_arg_raises_error(self):
        user = User()
        with self.assertRaises(TypeError):
            user.to_dict(None)


if __name__ == "__main__":
    unittest.main()
