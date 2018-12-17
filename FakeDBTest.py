import os
import unittest
from fakedb import FakeDB


class FileUtilsTest(unittest.TestCase):

    def test_it_creates_new_objects(self):
        """
        Test that fakedb creates new objects
        """
        db = FakeDB()
        db.create("name","Test")
        obj1 = db.get_object()
        obj2 = {"name":"Test"}
        self.assertEqual(obj1,obj2)

    def test_it_clears_an_object(self):
        """Test that fakedb clears an object successfully"""
        db = FakeDB()
        db.create("name","Test")
        id = db.commit('test.json')
        db.delete(id)
        self.assertEqual(1,len(db.get_object_by_id(id)))
        os.remove('test.json')


if __name__ == '__main__':
    unittest.main()
