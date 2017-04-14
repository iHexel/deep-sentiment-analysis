"""Preliminary Word2Vec modeling for each day in time period."""
import logging
from gensim.models import Word2Vec
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s',
                    level=logging.INFO)

# Set values for various parameters
num_features = 300    # Word vector dimensionality
min_word_count = 40   # Minimum word count
num_workers = 4       # Number of threads to run in parallel
context = 4          # Context window size
downsampling = 1e-3   # Downsample setting for frequent words

# list of unique days
days = (df_en.Day.unique()).tolist()

# dictionary with day as key and a list of words as values
daily_similar_words = dict.fromkeys(days)

# loop through all unique days
for i in days:
    # subset by day
    tmpdf = df_en[df_en['Day'] == i]

    # create new vector of just the text
    sentences = tmpdf['cleaned_text']

    # this is where the magic happens----word2vec model
    model = Word2Vec(sentences, workers=num_workers, size=num_features,
                     min_count=min_word_count, window=context, sample=downsampling)

    # makes the model more memory efficient
    model.init_sims(replace=True)

    # save the resulting words to a dictionary with the key being the day
    daily_similar_words[i] = model.most_similar_cosmul("trump", topn=50)
