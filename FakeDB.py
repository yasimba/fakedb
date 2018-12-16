import os
import sys
import uuid
sys.path.append(os.path.join(os.path.dirname(__file__), ".", ".."))
from fakedb.utils import FileUtils as utils
import json

class FakeDB(object):
    """Interface for creating and managing new objects"""

    def __init__(self):
        self.objects = {}
        self.obj = {}

    def create(self,k,v):
        """Creates a new object
        :type k: any
        :type v: any
        :param k: key for specific field
        :param v: value for specific field
        :return: void
        """
        self.obj[k] = v

    def update(self,k):
        """Update an existing object
        :type k: int
        param k: key of dictionary to update
        """

    def commit(self,f_name):
        """Adds new object to memory
        :type f_name: str
        :param f_name: name of file to insert object in
        """
        #prevent duplicate entries, clear list and start afresh
        self.objects = {}
        #generate 4-character id
        id = str(uuid.uuid4())[:8]
        self.objects[id] = self.obj
        utils.write_to_file(self,f_name,json.dumps(self.objects))

    def get_object(self):
        """Returns current object
        """
        return self.obj

    def get_objects(self):
        """Returns all objects committed
        """
        return self.objects
