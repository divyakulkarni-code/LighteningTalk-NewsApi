from newsapi import NewsApiClient
#from key import my_api_key
import datetime as dt
#import pandas as pd


# Init
newsapi = NewsApiClient(api_key='d29330c11283493c8febf5f7c3cecabc')

# /v2/top-headlines
# top_headlines = newsapi.get_top_headlines(q='bitcoin',
#                                           sources='bbc-news,the-verge',
#                                           category='business',
#                                           language='en',
#                                           country='us')

# /v2/everything
all_articles = newsapi.get_everything(q='Corona Virus',
                                      language='en',
                                      page=2)

# /v2/sources
#sources = newsapi.get_sources()

print(type(all_articles))

articles = all_articles['articles']

print(articles[0])

for article in articles:
    
    print(article['source']['name'],article['url'])

#print(all_articles['articles'][0]['url'])


