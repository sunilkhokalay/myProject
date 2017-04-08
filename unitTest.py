import unittest,logging,os
log = logging.getLogger(__name__)
logging.basicConfig(filename="C:\git\myProject\log.txt",level=logging.DEBUG,)

class TestCase(unittest.TestCase):
    def setUp(self):
        log.info("This is the Setup section!!")

    def test_Test1(self):
        log.info("This is the test step 1")

    def test_Test2(self):
        log.info("This is the test step 2")

    def tearDown(self):
        log.info("This is the Tear down section!!")

if __name__ == '__main__':
    unittest.main()
