from mockito import mock, verify
import unittest

import sys
import os.path
sys.path.append('C:\\Users\\nnagaraj\\L00179216_GitDemo\\src\\')
print("SYS : ", sys.path)
print("hh")
from dev import helloworld

class HelloWorldTest(unittest.TestCase):
    def test_should_issue_hello_world_message(self):
        out = mock()
        helloworld.helloworld(out)
        print("\n=========== TEST execution ========\n")
        verify(out).write("Hello world of Python\n")
