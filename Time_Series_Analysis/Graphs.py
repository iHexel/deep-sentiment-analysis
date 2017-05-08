"""Graphs verifying results"""
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
# Validation Series
from Validation_Series import valid_approval, valid_disapproval

# created series
from Deep_Sentiment_Analysis.Sentiment_Analysis.Daily_Sentiment import approval_rating_series, disapproval_rating_series

# sort index values
approval_rating_series.sort_index(inplace=True)
disapproval_rating_series.sort_index(inplace=True)

# remove first day of observations (test run)
approval_rating_series = approval_rating_series.drop(approval_rating_series.index[[0]])
disapproval_rating_series = disapproval_rating_series.drop(disapproval_rating_series.index[[0]])

####### Approval Ratings #######
fig = plt.figure(dpi=96)
ts = fig.add_subplot(1, 1, 1)

# format of xlabel
plt.xlabel('Day', fontsize='small')

# format of ylabel
plt.ylabel('Approval Rating', fontsize=8)
plt.ylim()
plt.title("Trump's Approval Ratings")

fig = valid_approval.plot(label="Valid (Rolling 3-Day Mean)", color='greenyellow')
fig = approval_rating_series.plot(label="Word2Vec (Daily)", color='r', linestyle='dashed', alpha=0.5)
fig = approval_rating_series.rolling(window=3, center=True).mean().plot(
    color='r', label='Word2Vec (Rolling 3-Day Mean)')
fig = ts.legend(loc='best')
plt.savefig('C:/Users/hexel/Documents/SYS 6016/Final Project/Deep_Sentiment_Analysis/Results/daily_approvals.jpg')

####### Disapproval Ratings #######
fig = plt.figure(dpi=96)
ts = fig.add_subplot(1, 1, 1)

# format of xlabel
plt.xlabel('Day', fontsize='small')

# format of ylabel
plt.ylabel('Disapproval Rating', fontsize=8)
plt.ylim()
plt.title("Trump's Disapproval Ratings")

fig = valid_disapproval.plot(label="Valid (Rolling 3-Day Mean)", color='darkgreen')
fig = disapproval_rating_series.plot(label="Word2Vec (Daily)", color='b', linestyle='dashed', alpha=0.5)
fig = disapproval_rating_series.rolling(window=3, center=True).mean().plot(
    color='b', label='Word2Vec (Rolling 3-Day Mean)')
fig = ts.legend(loc='best')
plt.savefig('C:/Users/hexel/Documents/SYS 6016/Final Project/Deep_Sentiment_Analysis/Results/daily_disapprovals.jpg')

####### Word2vec spread #######
fig = plt.figure(dpi=96)
ts = fig.add_subplot(1, 1, 1)

# format of xlabel
plt.xlabel('Day', fontsize='small')

# format of ylabel
plt.ylabel('Approval Rating vs Disapproval Rating', fontsize=8)
plt.ylim()
plt.title("Trump's Ratings Overall")

fig = disapproval_rating_series.rolling(window=3, center=True).mean().plot(
    color='b', label='Word2Vec Disapproval')
fig = valid_disapproval.plot(label="Valid Disapproval", color='darkgreen')
fig = approval_rating_series.rolling(window=3, center=True).mean().plot(
    color='r', label='Word2Vec Approval')
fig = valid_approval.plot(label="Valid Approval", color='greenyellow')
lgd = ts.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.savefig('C:/Users/hexel/Documents/SYS 6016/Final Project/Deep_Sentiment_Analysis/Results/daily_comparison.jpg', bbox_extra_artists=(lgd,), bbox_inches='tight')
