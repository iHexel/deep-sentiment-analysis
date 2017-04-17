"""Word2Vec modeling for each state in country by day"""
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

# list of unique combinations of days and states
combos = list(set(zip(df_en.Day, df_en.region)))

# dictionary with state as key and a list of words as values
region_similar_words = dict.fromkeys(combos)

# loop through all unique states
for combo in combos:
    # subset by state
    tmpdf = df_en[(df_en['Day']==combo[0]) & (df_en['region']==combo[1])]

    # create new vector of just the text
    sentences = tmpdf['cleaned_text']

    # this is where the magic happens----word2vec model
    model = Word2Vec(sentences, workers=num_workers, size=num_features,
                     min_count=min_word_count, window=context, sample=downsampling)

    # makes the model more memory efficient
    model.init_sims(replace=True)

    # save the resulting words to a dictionary with the key being the state
    region_similar_words[combo] = model.most_similar_cosmul("trump", topn=2000)
