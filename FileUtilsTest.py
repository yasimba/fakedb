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
        futils.write_to_file(self,"tests/"+file1,data)
        futils.write_to_file(self,"tests/"+file2,data)
        dir = os.path.dirname(os.path.abspath(__file__))
        self.assertTrue(filecmp.cmp(os.path.join(dir,file2), os.path.join(dir,file1)))
        os.remove(file2)
        os.remove(file1)

if __name__ == '__main__':
    unittest.main()
