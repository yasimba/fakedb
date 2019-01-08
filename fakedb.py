import uuid
from utils import FileUtils as utils
import json

class FakeDB(object):
    """Interface for creating and managing new objects"""

    def __init__(self):
        self.objects = dict()
        self.obj = dict()

    def create(self,k,v):
        """Creates a new object
        :type k: any
        :type v: any
        :param k: key for specific field
        :param v: value for specific field
        :return: void
        """
        self.obj[k] = v

    def load_from(file_path):
        """loads data from a defined file path
        :type file_path: str
        :param file_path: path from which to read data
        :return list
        """
        return utils.read_from_file(file_path)

    def remove(file_path):
        utils.delete_file(file_path)


    def update(self,id,data):
        """Update an existing object
        :type id: str
        param id: id of dictionary to update
        :type data: object
        :param data: dictionary to update object with
        """
        self.objects[id].update(data)

    def clear(self,id):
        """Clear the contents of an object
        :type id: str
        param id: id of dictionary to delete
        return: void
        """
        self.objects[id].clear()

    def commit(self,f_name):
        """Adds new object to memory
        :type f_name: str
        :param f_name: name of file to insert object in
        return: id of commited object
        """
        #prevent duplicate entries, clear list and start afresh
        self.objects = dict()
        #generate 4-character id
        id = str(uuid.uuid4())[:8]
        self.objects[id] = self.obj
        utils.write_to_file(f_name,json.dumps(self.objects))
        return id

    def get_object(self):
        """Returns current object
        """
        return self.obj

    def get_object_by_id(self,id):
        """Returns object given the id
        """
        return self.objects[id]

    def get_objects(self):
        """Returns all objects committed
        """
        return self.objects
