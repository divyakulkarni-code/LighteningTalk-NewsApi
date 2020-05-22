from flask import Flask, redirect, request, render_template, session
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined
from newsapi import NewsApiClient
import datetime as dt


app = Flask(__name__)

# This option will cause Jinja to throw UndefinedErrors if a value hasn't
# been defined (so it more closely mimics Python's behavior)
app.jinja_env.undefined = StrictUndefined

# This option will cause Jinja to automatically reload templates if they've been
# changed. This is a resource-intensive operation though, so it should only be
# set while debugging.
app.jinja_env.auto_reload = True

# Required to use Flask sessions and the debug toolbar
app.secret_key = 'ABC'
#'e056ea8ab79d4521a6bea31a56b86446' d29330c11283493c8febf5f7c3cecabc
newsapi = NewsApiClient(api_key='e056ea8ab79d4521a6bea31a56b86446')


@app.route("/")
def index():
    '''Return Home page'''
    return render_template("Presentation.html")


@app.route("/news-api")
def view_news():
    '''Displaying my API used'''
    return render_template("Api_used.html")   
        


@app.route("/demonstration-api")
def demo_api():
    all_articles = newsapi.get_everything(q='New york',
                                            language='en',
                                            page=2)

    articles = all_articles['articles']
       
    return render_template("Demonstration.html", articles=articles)



if __name__ == '__main__':
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    DebugToolbarExtension(app)

    app.run(host='0.0.0.0')
