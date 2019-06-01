import pandas as pd
import re

csvfilepath = input('csv filepath : ')
df = pd.read_csv(csvfilepath)

tweets = df['text']

replypattern = '@[\w]+'
urlpattern = 'https?://[\w/:%#\$&\?\(\)~\.=\+\-]+'
moviepattern = '\[動画\]'
picturepattern = '\[写真\]'
stickerpattern = '\[スタンプ\]'
notepattern = '\[ノート\]'

processedtweets = []

for tweet in tweets:
    i = re.sub(replypattern, '', tweet)
    i = re.sub(urlpattern, '', i)
    i = re.sub(moviepattern, '', i)
    i = re.sub(picturepattern, '', i)
    i = re.sub(stickerpattern, '', i)
    i = re.sub(notepattern, '', i)
    if isinstance(i, str) and not i.split():
        pass
    else:
        processedtweets.append(i)

processedtweetsDataFrame = pd.Series(processedtweets)
newDF = pd.DataFrame({'text': processedtweetsDataFrame})

newDF.to_csv('processed.csv')