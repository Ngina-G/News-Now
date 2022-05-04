class Article:
    
    def __init__(self,author,title,description,url,urlToImage,content,publishedAt):
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.content = content
        self.content = publishedAt

class Source:
    source = []
    
    def __init__(self,name,id):
        self.name = name
        self.id = id