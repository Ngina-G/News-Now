from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_articles, get_article, get_source

@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'Welcome to NewsNow the best News Website'
    # articles = get_articles('business')
    general_source = get_articles('general')
    business_source = get_articles('business')
    health_source = get_articles('health')
    tech_source = get_articles('technology')

    return render_template('index.html',title=title,general= general_source,business=business_source,health=health_source,technology=tech_source)

@main.route('/articles')
def articles():
    '''
    View article page function that returns the articles
    '''
    title = f'Articles from {source.name}'
    articles = get_articles(category)
    return render_template('articles.html',title=title,articles=articles)

@main.route('/detail/<int:title>')
def detail(title):
    '''
    View article page function that returns the articles
    '''
    title = f'{article.title}'
    detail = get_article(title)
    return render_template('detail.html',title=title,detail=detail)