"""Measuring Sentiment of Tweets by State (Overall)"""
import nltk
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
# lexicon file needed by SentimentIntensityAnalyzer
# nltk.download('vader_lexicon')
# import daily_similar_words

# shortening analyzer function call
sid = SentimentIntensityAnalyzer()

# grab keys of dictionary
combos = region_similar_words.keys()

# Initialize an approval ratings Series
approval_rating_series = pd.Series()

# Initialize a disapproval ratings Series
disapproval_rating_series = pd.Series()

# loop through all combos
for combo in combos:

    # check if length of list of words for a given state is 0, skip if true
    if len(region_similar_words[combo]) == 0:
        continue

    # Initialize lists
    positive_words = []
    negative_words = []

    # loop through the length of the list
    for i in range(len(region_similar_words[combo])):

        # grab an element of list and then grab the first element of that element
        tmp = region_similar_words[combo][i][0]

        # score the word
        scores = sid.polarity_scores(tmp)

        # list of positive scores
        positive_words.append(scores["pos"])

        # list of negative scores
        negative_words.append(scores["neg"])

    # sum over the lists
    positive = sum(positive_words)
    negative = sum(negative_words)

    # check if sum is 0, skip further calculations if true
    if positive == 0 or negative == 0:
        continue

    # calculate simple approval rating from previous sums
    approval_rating = positive / (positive + negative)

    # calculate simple disapproval rating from previous sums
    disapproval_rating = negative / (positive + negative)

    # append the new results as a series to the original series
    approval_rating_series = approval_rating_series.append(pd.Series(approval_rating, index=[combo]))
    disapproval_rating_series = disapproval_rating_series.append(
        pd.Series(disapproval_rating, index=[combo]))
