import unittest
from app.models import Source

class SourceTest(unittest.TestCase()):
    """
    Test Class to test the behaviour of the Source class
    """
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Source("Business Insider","business-insider")

    def test_init(self):
        self.assertEqual(self.new_name,"Business Insider")
        self.assertEqual(self.new_id,"business-insider")
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_source, Source))