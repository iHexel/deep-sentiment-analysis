"""Measuring Sentiment of Tweets by Day"""
import pandas as pd
import nltk
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
# lexicon file needed by SentimentIntensityAnalyzer
# nltk.download('vader_lexicon')
# import daily_similar_words

# shortening analyzer function call
sid = SentimentIntensityAnalyzer()

# grab keys of dictionary
days = daily_similar_words.keys()

# Initialize an approval ratings Series
approval_rating_series = pd.Series()

# Initialize a disapproval ratings Series
disapproval_rating_series = pd.Series()

# loop through all days
for day in days:

    # Initialize lists
    positive_words = []
    negative_words = []

    # loop through the length of the list
    for i in range(0, len(daily_similar_words[day])):

        # grab an element of list and then grab the first element of that element
        tmp = daily_similar_words[day][i][0]

        # score the word
        scores = sid.polarity_scores(tmp)

        # list of positive scores
        positive_words.append(scores["pos"])

        # list of negative scores
        negative_words.append(scores["neg"])

    # sum over the lists
    positive = sum(positive_words)
    negative = sum(negative_words)

    # calculate simple approval rating from previous sums
    approval_rating = positive / (positive + negative)

    # calculate simple disapproval rating from previous sums
    disapproval_rating = negative / (positive + negative)

    # append the new results as a series to the original series
    approval_rating_series = approval_rating_series.append(
        pd.Series(approval_rating, index=[day]))
    disapproval_rating_series = disapproval_rating_series.append(
        pd.Series(disapproval_rating, index=[day]))
