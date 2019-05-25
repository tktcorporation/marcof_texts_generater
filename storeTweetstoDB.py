from PrepareChain import *
import pandas as pd
from tqdm import tqdm
import sys

def storeTweetstoDB():

    if len(sys.argv) > 2:
        df = pd.read_csv(sys.argv[1])
    else:
        csvfilepath = input('tweets.csv filepath : ')
        df = pd.read_csv(csvfilepath)


    tweets = df['text']

    print(len(tweets))

    chain = PrepareChain(tweets[0])
    triplet_freqs = chain.make_triplet_freqs()
    chain.save(triplet_freqs, True)

    for i in tqdm(tweets[1:]):
        chain = PrepareChain(i)
        triplet_freqs = chain.make_triplet_freqs()
        chain.save(triplet_freqs, False)



if __name__ == '__main__':
    storeTweetstoDB()