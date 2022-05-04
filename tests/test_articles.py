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

    def test_check_initialization(self):
        self.assertEquals(self.new_article.author, )
        self.assertEquals(self.new_article.title, )
        self.assertEquals(self.new_article.description, )
        self.assertEquals(self.new_article.url, )
        self.assertEquals(self.new_article.urlToImage, )
        self.assertEquals(self.new_article.content, )
        self.assertEquals(self.new_article.publishedAt, )
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))