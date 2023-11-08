from mockito import mock, verify
import unittest

import sys
import os.path
sys.path.append('/home/runner/work/L00179216_GitDemo/L00179216_GitDemo/dev')
print("SYS : ", sys.path)

from dev import helloworld
from ATUapp import hellow_msg

class WebAppTest(unittest.TestCase):
    """
    This is the webApp test module covers multiple testcases
    to test the functionality
    """
    def test_hello_world_reponse_message(self):
        """
        This is the test method to validate the response 
        of helloworld app 
        """
        out = mock()
        helloworld.helloworld(out)
        print("\n=========== TEST1 execution ========\n")
        verify(out).write("Hello world of DevOps\n")

    def test_atuapp_response_message(self, name="Nayana"):
        """
        This is the test method to check the message of ATUapp
        """
        print("\n=========== TEST2 execution ========\n")
        assert hellow_msg() == f"HELLO, WELCOME TO ATU LETTERKENNY UNIVERSITY {name}!!!"
