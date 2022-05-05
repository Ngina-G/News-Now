import unittest
from app.models import Source

class SourceTest(unittest.TestCase):
    """
    Test Class to test the behaviour of the Source class
    """
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Source("Business Insider","business-insider","http//:")

    def test_init(self):
        self.assertEqual(self.new_source.name,"Business Insider")
        self.assertEqual(self.new_source.id,"business-insider")
        self.assertEqual(self.new_source.sourceUrl,"http//:")
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_source, Source))