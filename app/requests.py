import urllib.request,json
from .models import Source
from .models import Article

# Getting api key
api_key = None

# Getting the movie base url
base_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']

# SOURCES
def get_source():
    '''
    Function that gets the json response to our url request for sources
    '''
    get_url = source_base_url.format(api_key)
    print (get_url)
    
    with urllib.request.urlopen(get_url) as url:
        get_data = url.read()
        get_sources_response = json.loads(get_data)
        
        source_result = None
        
        if get_sources_response['sources']:
            source_result_list = get_sources_response['sources']
            source_result = process_results(source_result_list)

    return source_result
        
def process_result(source_result_list):
    '''
    Function that processes sources
    '''
    source_result = []
    for item in source_result_list:
        name = item.get('name')
        url = item.get('url')
        
        source_object = Source(name,url) 
        source_result.append(source_object)
    return source_result

# ARTICLES
def get_articles(category):
    '''
    Function that gets the json response to our url request for articles
    '''
    get_url = base_url.format(category,api_key)
    
    with urllib.request.urlopen(get_url) as url:
        get_data = url.read()
        get_article_response = json.loads(get_data)
        
        article_result = None
        
        if get_article_response['articles']:
            article_result_list = get_article_response['articles']
            article_result = process_results(article_result_list)
    return article_result

def get_article(id):

    get_article_details_url = base_url.format(id,api_key)
    
    with urllib.request.urlopen(get_article_details_url) as url:
        article_details_data = url.read()
        article_details_response = json.loads(article_details_data)
        
        article_object = None
        
        if article_details_response:
            author = article_details_response.get('author')
            title = article_details_response.get('title')
            description = article_details_response.get('description')
            url = article_details_response.get('url')
            urlToImage = article_details_response.get('urlToImage')
            content = article_details_response.get('content')
            publishedAt = article_details_response.get('publishedAt')

            article_object = Article(author,title,description,url,urlToImage,content,publishedAt)
    return article_object

def process_results(article_list):
    article_result = []
    '''
        Function  that processes the article result and transform them to a list of Objects
        Args:
            article_list: A list of dictionaries that contain aricle details
        Returns :
            article_results: A list of article objects
    '''
    for item in article_list:
        author = item.get('author')
        title = item.get('title')
        description = item.get('description')
        url = item.get('url')
        urlToImage = item.get('urlToImage')
        content = item.get('content')
        publishedAt = item.get('publishedAt')
        
        article_object = Article(author,title,description,url,urlToImage,content,publishedAt)
        article_result.append(article_object)
    return article_result

