import markovify
import os

dirname = os.path.dirname(os.path.abspath(__file__))
tweets = os.path.join(dirname, 'tweets.txt')

with open(tweets) as f:
    text = f.read()

text_model = markovify.Text(text)

print(text_model.make_short_sentence(280))