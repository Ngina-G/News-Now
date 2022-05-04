import unittest
from app.models import Article

class ArticleTest(unittest.TestCase()):
    """
    Test Class to test the behaviour of the Article class
    """
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Article("JohnDoe","TeslaStock","Stock is up","http://","http://","content","date")

    def test_init(self):
        self.assertEqual(self.new_user.f_name,"John")
        self.assertEqual(self.new_user.l_name,"Doe")
        self.assertEqual(self.new_user.u_name,"John Doe")
        self.assertEqual(self.new_user.email,"pseudo@gmail.com")
        self.assertEqual(self.new_user.password,"123john")
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))