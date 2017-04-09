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

    def test_testCase1(self):
        log.info("This is the test case 1")

    def test_testCase2(self):
        log.info("This is the test case 2")

    def tearDown(self):
        log.info("This is the Test Case Tear down section!!")


if __name__ == '__main__':
    unittest.main()
    # suite = unittest.TestSuite()
    # suite.addTest(TestCase('test_testCase1'))
    # runner = unittest.TextTestRunner()
    # runner.run(suite)
