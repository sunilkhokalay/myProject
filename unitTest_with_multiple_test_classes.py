import unittest,logging
log = logging.getLogger(__name__)
logging.basicConfig(filename="C:\git\myProject\log.txt",level=logging.DEBUG,)

class TestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        log.info("This is the Common setup")

    @classmethod
    def tearDownClass(cls):
        log.info("This is the Common clean up.")

    def setUp(self):
        log.info("This is the Test Case Setup section!!")

    def test_testCase1_1(self):
        log.info("This is the test case 1 of 1 ")

    def test_testCase2_1(self):
        log.info("This is the test case 2 of 1")

    def tearDown(self):
        log.info("This is the Test Case Tear down section!!")

class TestCase2(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        log.info("This is the Common setup")

    @classmethod
    def tearDownClass(cls):
        log.info("This is the Common clean up.")

    def setUp(self):
        log.info("This is the Test Case Setup section!!")

    def test_testCase1_2(self):
        log.info("This is the test case  of 2 ")

    def test_testCase2_2(self):
        log.info("This is the test case 2 of 2")

    def tearDown(self):
        log.info("This is the Test Case Tear down section!!")





if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCase))
    suite.addTest(unittest.makeSuite(TestCase2))
    runner = unittest.TextTestRunner()
    runner.run(suite)


