import os
import sys

class FileUtils(object):
    """Utilities for working with files"""

    def read_from_file(file_path):
        """Read database from file reference
        :type file_path: str
        :param file_path: file from which to read from
        :return string
        """
        data = []
        #TODO: use as decorator
        if(not os.path.isfile(file_path)):
            print("{} does not exist".format(file_path))
            return

        try:
            with open(file_path, "r") as path:
                data.append(path.read())
                return data
        except IOError:
            return "Unable to read from path"
            sys.exit()

    def delete_file(file_path):
        """Remove a file in the specified path
        :type file_path: str
        :param file_path: file from which to remove
        """
        if(not os.path.isfile(file_path)):
            print("{} does not exist".format(file_path))
            return
        try:
            os.remove(file_path)
        except:
            return "Error removing file"

    def write_to_file(file, data):
        """Writes the data to the predefined file
        :type file: str
        :param word: file to write the data to
        :type data: object
        :param data: data to write in the file
        :return: void
        """
        if file.lower().endswith(('.json')) is False:
            return "Invalid file format, must end with .json"
        dir = os.path.dirname(os.path.abspath(__file__))
        f_name = os.path.join(dir, file)
        try:
            with open(f_name, "a+") as f_write:
                f_write.write(data)
        except IOError:
            print("Unable to write to file")
            sys.exit()
