"""Graphs for sentiment analysis by state"""
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

# created series
from Deep_Sentiment_Analysis.Sentiment_Analysis.Statewide_Sentiment import approval_rating_series, disapproval_rating_series

# sort index values
approval_rating_series.sort_index(inplace=True)
disapproval_rating_series.sort_index(inplace=True)

####### Approval Ratings #######
top10_approve = approval_rating_series.sort_values().tail(n=10).sort_values(ascending=False)
top10_disapprove = disapproval_rating_series.sort_values().tail(n=10).sort_values(ascending=False)
