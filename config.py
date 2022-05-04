import os

class Config:
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/top-headlines/sources?apiKey=572b2c89c2ad46859d50e753d3fb6f1b'
    ARTICLES_BASE_URL ='https://newsapi.org/v2/top-headlines?country=us&category={}&apiKey={}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')

    @staticmethod
    def init_app(app):
        pass


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig

}