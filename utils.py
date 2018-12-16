import os
import sys

class FileUtils(object):
    """Utilities for working with files"""

    def write_to_file(self,file,data):
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
        f_name = os.path.join(dir,file)
        try:
            with open(f_name,"a+") as f_write:
                f_write.write(data)
        except IOError:
            print("Unable to write to file")
            sys.exit()
