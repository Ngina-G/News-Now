class Article:
    
    def __init__(self,author,title,description,url,urlToImage,content,publishedAt):
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.content = content
        self.publishedAt = publishedAt

class Source:
    
    def __init__(self,name,id,url):
        self.name = name
        self.id = id
        self.sourceUrl = url