import urllib.request,json
from .models import Source
from .models import Article

# Getting api key
api_key = None

# Getting the source url
base_url = None

# Getting the articles from a source url
articles_base_url = None

def configure_request(app):
    global api_key,base_url,articles_base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
    articles_base_url = app.config['ARTICLES_BASE_URL']

# SOURCES
def get_source(category):
    '''
    Function that gets the json response to our url request for sources
    '''
    get_url = base_url.format(category,api_key)
    
    with urllib.request.urlopen(get_url) as url:
        get_data = url.read()
        get_sources_response = json.loads(get_data)
        
        source_result = None
        
        if get_sources_response['sources']:
            source_result_list = get_sources_response['sources']
            source_result = process_result(source_result_list)

    return source_result
        
def process_result(source_list):
    '''
    Function that processes sources
    '''
    source_result = []
    for item in source_list:
        name = item.get('name')
        sourceUrl = item.get('sourceUrl')
        
        source_object = Source(name,id,sourceUrl) 
        source_result.append(source_object)
    return source_result

# ARTICLES
def get_articles(id):

    get_article_details_url = articles_base_url.format(id)
    get_article_detail_url = get_article_details_url.replace(' ','-')
    
    with urllib.request.urlopen(get_article_detail_url) as url:
        get_data = url.read()
        get_article_response = json.loads(get_data)
        
        article_result = None
        
        
        if get_article_response['articles']:
            article_result_list = get_article_response['articles']
            article_result = process_results(article_result_list)
            print(article_result)
    return article_result

def process_results(article_list):
    '''
        Function  that processes the article result and transform them to a list of Objects
        Args:
            article_list: A list of dictionaries that contain aricle details
        Returns :
            article_results: A list of article objects
    '''
    article_result = []
    article_object = None

    for item in article_list:
        author = item.get('author')
        title = item.get('title')
        description = item.get('description')
        url = item.get('url')
        urlToImage = item.get('urlToImage')
        content = item.get('content')
        publishedAt = item.get('publishedAt')
        
        # if urlToImage:
        article_object = Article(author,title,description,url,urlToImage,content,publishedAt)
        article_result.append(article_object)
    return article_result

