import unittest
from app.models import Article

class ArticleTest(unittest.TestCase):
    """
    Test Class to test the behaviour of the Article class
    """
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Article("JohnDoe","TeslaStock","Stock is up","http://","http://","content","date")

    def test_check_initialization(self):
        self.assertEquals(self.new_article.author, "JohnDoe")
        self.assertEquals(self.new_article.title, "TeslaStock")
        self.assertEquals(self.new_article.description, "Stock is up")
        self.assertEquals(self.new_article.url, "http://")
        self.assertEquals(self.new_article.urlToImage, "http://")
        self.assertEquals(self.new_article.content, "content")
        self.assertEquals(self.new_article.publishedAt, "date")
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))