"""Graphs for sentiment analysis by region"""
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

# created series
from Deep_Sentiment_Analysis.Sentiment_Analysis.Daily_Sentiment_by_Region import approval_rating_series, disapproval_rating_series

# create series for each region
ars_midwest = pd.Series()
ars_west = pd.Series()
ars_south = pd.Series()
ars_northeast = pd.Series()
drs_midwest = pd.Series()
drs_west = pd.Series()
drs_south = pd.Series()
drs_northeast = pd.Series()

# assign the approval rating to proper region based on date
for day in days:
    ars_midwest[day] = approval_rating_series[(day, 'MIDWEST')]
    ars_west[day] = approval_rating_series[(day, 'WEST')]
    ars_south[day] = approval_rating_series[(day, 'SOUTH')]
    ars_northeast[day] = approval_rating_series[(day, 'NORTHEAST')]
    drs_midwest[day] = disapproval_rating_series[(day, 'MIDWEST')]
    drs_west[day] = disapproval_rating_series[(day, 'WEST')]
    drs_south[day] = disapproval_rating_series[(day, 'SOUTH')]
    drs_northeast[day] = disapproval_rating_series[(day, 'NORTHEAST')]

# sort dates in descending order
ars_midwest.sort_index(inplace=True)
ars_west.sort_index(inplace=True)
ars_south.sort_index(inplace=True)
ars_northeast.sort_index(inplace=True)
drs_midwest.sort_index(inplace=True)
drs_west.sort_index(inplace=True)
drs_south.sort_index(inplace=True)
drs_northeast.sort_index(inplace=True)

# remove observations for April 1st (trial date)
ars_midwest = ars_midwest.drop(ars_midwest.index[[0]])
ars_west = ars_west.drop(ars_west.index[[0]])
ars_south = ars_south.drop(ars_south.index[[0]])
ars_northeast = ars_northeast.drop(ars_northeast.index[[0]])
drs_midwest = drs_midwest.drop(drs_midwest.index[[0]])
drs_west = drs_west.drop(drs_west.index[[0]])
drs_south = drs_south.drop(drs_south.index[[0]])
drs_northeast = drs_northeast.drop(drs_northeast.index[[0]])

####### Approval Ratings #######
fig = plt.figure(dpi=96)
ts = fig.add_subplot(1, 1, 1)

# format of xlabel
plt.xlabel('Day', fontsize='small')

# format of ylabel
plt.ylabel('Approval Rating', fontsize=8)
plt.ylim()
plt.title("Trump's Approval Ratings by Region")

fig = ars_northeast.plot(label="Northeast (Daily)", color='b', linestyle='dashed', alpha=0.3)
fig = ars_northeast.rolling(window=3, center=True).mean().plot(
    color='b', label='Northeast (Rolling 3-Day Mean)')
fig = ars_south.plot(label="South (Daily)", color='r', linestyle='dashed', alpha=0.3)
fig = ars_south.rolling(window=3, center=True).mean().plot(
    color='r', label='South (Rolling 3-Day Mean)')
fig = ars_midwest.plot(label="Midwest (Daily)", color='y', linestyle='dashed', alpha=0.3)
fig = ars_midwest.rolling(window=3, center=True).mean().plot(
    color='y', label='Midwest (Rolling 3-Day Mean)')
fig = ars_west.plot(label="West (Daily)", color='g', linestyle='dashed', alpha=0.3)
fig = ars_west.rolling(window=3, center=True).mean().plot(
    color='g', label='West (Rolling 3-Day Mean)')

lgd = ts.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

plt.savefig('C:/Users/hexel/Documents/SYS 6016/Final Project/Deep_Sentiment_Analysis/Results/regional_approvals.jpg', bbox_extra_artists=(lgd,), bbox_inches='tight')


####### Disapproval Ratings #######
fig = plt.figure(dpi=96)
ts = fig.add_subplot(1, 1, 1)

# format of xlabel
plt.xlabel('Day', fontsize='small')

# format of ylabel
plt.ylabel('Disapproval Rating', fontsize=8)
plt.ylim()
plt.title("Trump's Disapproval Ratings by Region")

fig = drs_northeast.plot(label="Northeast (Daily)", color='b', linestyle='dashed', alpha=0.3)
fig = drs_northeast.rolling(window=3, center=True).mean().plot(
    color='b', label='Northeast (Rolling 3-Day Mean)')
fig = drs_south.plot(label="South (Daily)", color='r', linestyle='dashed', alpha=0.3)
fig = drs_south.rolling(window=3, center=True).mean().plot(
    color='r', label='South (Rolling 3-Day Mean)')
fig = drs_midwest.plot(label="Midwest (Daily)", color='y', linestyle='dashed', alpha=0.3)
fig = drs_midwest.rolling(window=3, center=True).mean().plot(
    color='y', label='Midwest (Rolling 3-Day Mean)')
fig = drs_west.plot(label="West (Daily)", color='g', linestyle='dashed', alpha=0.3)
fig = drs_west.rolling(window=3, center=True).mean().plot(
    color='g', label='West (Rolling 3-Day Mean)')

lgd = ts.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

plt.savefig('C:/Users/hexel/Documents/SYS 6016/Final Project/Deep_Sentiment_Analysis/Results/regional_disapprovals.jpg', bbox_extra_artists=(lgd,), bbox_inches='tight')


####### Word2vec spread #######
fig = plt.figure(dpi=96)
ts = fig.add_subplot(1, 1, 1)

# format of xlabel
plt.xlabel('Day', fontsize='small')

# format of ylabel
plt.ylabel('Approval Rating vs Disapproval Rating', fontsize=8)
plt.ylim()
plt.title("Trump's Regional Ratings")

fig = drs_northeast.rolling(window=3, center=True).mean().plot(
    color='darkblue', label='Northeast (Rolling 3-Day Mean)')
fig = drs_south.rolling(window=3, center=True).mean().plot(
    color='royalblue', label='South (Rolling 3-Day Mean)')
fig = drs_midwest.rolling(window=3, center=True).mean().plot(
    color='cornflowerblue', label='Midwest (Rolling 3-Day Mean)')
fig = drs_west.rolling(window=3, center=True).mean().plot(
    color='lightblue', label='West (Rolling 3-Day Mean)')
fig = valid_disapproval.plot(label="Valid Disapproval", color='darkgreen')

fig = ars_northeast.rolling(window=3, center=True).mean().plot(
    color='firebrick', label='Northeast (Rolling 3-Day Mean)')
fig = ars_south.rolling(window=3, center=True).mean().plot(
    color='indianred', label='South (Rolling 3-Day Mean)')
fig = ars_midwest.rolling(window=3, center=True).mean().plot(
    color='tomato', label='Midwest (Rolling 3-Day Mean)')
fig = ars_west.rolling(window=3, center=True).mean().plot(
    color='sandybrown', label='West (Rolling 3-Day Mean)')
fig = valid_approval.plot(label="Valid Approval", color='greenyellow')

lgd = ts.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

plt.savefig('C:/Users/hexel/Documents/SYS 6016/Final Project/Deep_Sentiment_Analysis/Results/regional_comparison.jpg', bbox_extra_artists=(lgd,), bbox_inches='tight')
