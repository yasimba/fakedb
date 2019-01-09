import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
import unittest
from utils import FileUtils as futils
import filecmp


class FileUtilsTest(unittest.TestCase):
    def test_file_write(self):
        """
        Test that file is written successfully
        """
        data = "ABCDEFG"
        file1 = "file.json"
        file2 = "f.json"
        futils.write_to_file(file1,data)
        futils.write_to_file(file2,data)
        dir = os.path.dirname(os.path.abspath(__file__))
        self.assertTrue(filecmp.cmp(os.path.join(dir,file2), os.path.join(dir,file1)))
        os.remove(file2)
        os.remove(file1)

    def test_file_read(self):
        """
        Test file read capability
        """
        data="{key:value}"
        file1 = "filew.json"
        futils.write_to_file(file1,data)
        ret = futils.read_from_file(file1)
        self.assertTrue(data,ret)
        os.remove(file1)


if __name__ == '__main__':
    unittest.main()
