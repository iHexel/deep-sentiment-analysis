"""Graphs verifying results"""
import matplotlib.pyplot as plt
%matplotlib inline
# Validation Series
from Validation_Series import valid_approval, valid_disapproval

# created series
from Deep_Sentiment_Analysis.Sentiment_Analysis.Daily_Sentiment import approval_rating_series, disapproval_rating_series

# sort index values
approval_rating_series.sort_index(inplace=True)
disapproval_rating_series.sort_index(inplace=True)

####### Approval Ratings #######
fig = plt.figure(dpi=300)
ts = fig.add_subplot(1, 1, 1)

# format of xlabel
plt.xlabel('Day', fontsize='small')

# format of ylabel
plt.ylabel('Approval Rating', fontsize=8)
plt.ylim()

fig = valid_approval.plot(label="Valid")
fig = approval_rating_series.plot(label="Word2Vec")
# fig = approval_rating_series.rolling(window=3, center=False).mean().plot(
#     color='#fc8d62', linestyle='dashed', label='Word2Vec Rolling 3 Day Mean')
fig = ts.legend(loc='best')

####### Disapproval Ratings #######
fig = plt.figure(dpi=300)
ts = fig.add_subplot(1, 1, 1)

# format of xlabel
plt.xlabel('Day', fontsize='small')

# format of ylabel
plt.ylabel('Disapproval Rating', fontsize=8)
plt.ylim()

fig = valid_disapproval.plot(label="Valid")
fig = disapproval_rating_series.plot(label="Word2Vec")
fig = ts.legend(loc='best')

####### Word2vec spread #######
fig = plt.figure(dpi=300)
ts = fig.add_subplot(1, 1, 1)

# format of xlabel
plt.xlabel('Day', fontsize='small')

# format of ylabel
plt.ylabel('Approval Rating vs Disapproval Rating', fontsize=8)
plt.ylim()

fig = disapproval_rating_series.plot(label="Disapproval")
fig = approval_rating_series.plot(label="Approval")
fig = ts.legend(loc='best')
