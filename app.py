from flask import Flask, render_template, flash, redirect, url_for, session, logging
from data import articles



app = Flask(__name__)
app.debug = True


Articles = articles()


@app.route('/')
def hello_world():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/articles')
def articles():
    return render_template('articles.html', articles=Articles)


@app.route('/article/<string:id>/')
def article(id):
    return render_template('article.html', id=id)

if __name__ == '__main__':
    app.run()
