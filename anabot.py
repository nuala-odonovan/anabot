import markovify
import os
import nltk
import re

dirname = os.path.dirname(os.path.abspath(__file__))
tweets = os.path.join(dirname, 'tweets.txt')

with open(tweets) as f:
    text = f.read()



class POSifiedText(markovify.Text):
    def word_split(self, sentence):
        words = re.split(self.word_split_pattern, sentence)
        words = [ "::".join(tag) for tag in nltk.pos_tag(words) ]
        return words

    def word_join(self, words):
        sentence = " ".join(word.split("::")[0] for word in words)
        return sentence


text_model = markovify.Text(text)

print(text_model.make_short_sentence(280))