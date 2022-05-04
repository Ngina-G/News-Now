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
    '''processes sources'''
    source_result = []
    for item in source_result_list:
        name = item.get('name')
        url = item.get('url')
        
        source_object = Source(name,url) 
        source_result.append(source_object)
    return source_result



