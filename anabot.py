import os
from markovbot import MarkovBot

anabot = MarkovBot()

dirname = os.path.dirname(os.path.abspath(__file__))
tweets = os.path.join(dirname, 'tweets.txt')

anabot.read(tweets)

a_tweet = anabot.generate_text(25, seedword=['chile'])
print(a_tweet)