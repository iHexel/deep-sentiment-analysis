# Deep Sentiment Analysis
Analyzing sentiment around the current presidential administration using Word2Vec.

# Summary
The goal of the project is to analyze the sentiment of words around the target word "trump". We plan to apply Word2Vec to a months worth of tweets and from that derive the most common words used with the target word. We will then apply sentiment analysis technique to these words and compare the results each day to the polled approval ratings.

# Data
We collected tweets with the the word "trump" for the month of April. We used the Twitter streaming API to listen for these tweets, extract the relevant information, and insert the results into an Postgres database.

# Collaborators
* Tyler Worthington
* Lev Zadvinskiy
