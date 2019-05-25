import pandas as pd
import re

df = pd.read_csv('./tweets/tweets.csv')

tweets = df['text']

replypattern = '@[\w]+'
urlpattern = 'https?://[\w/:%#\$&\?\(\)~\.=\+\-]+'

processedtweets = []

for tweet in tweets:
    i = re.sub(replypattern, '', tweet)
    i = re.sub(urlpattern, '', i)
    if isinstance(i, str) and not i.split():
        pass
    else:
        processedtweets.append(i)

processedtweetsDataFrame = pd.Series(processedtweets)
newDF = pd.DataFrame({'text': processedtweetsDataFrame})

newDF.to_csv('processedtweets.csv')