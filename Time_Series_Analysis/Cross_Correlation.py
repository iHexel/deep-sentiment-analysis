"""Analyzing cross correlation between time series"""
# http://statsmodels.sourceforge.net/stable/generated/statsmodels.tsa.stattools.ccf.html#statsmodels.tsa.stattools.ccf
import numpy as np
from statsmodels.tsa.stattools import ccf
import statistics as stat
import matplotlib.pyplot as plt
%matplotlib inline
# Validation Series
from Validation_Series import valid_approval, valid_disapproval

# created series
from Deep_Sentiment_Analysis.Sentiment_Analysis.Daily_Sentiment import approval_rating_series, disapproval_rating_series

# sort index values
approval_rating_series.sort_index(inplace=True)
disapproval_rating_series.sort_index(inplace=True)

fig = plt.figure()
ax1 = fig.add_subplot(211)

#cross correlations
ax1.xcorr(approval_rating_series, valid_approval,
          usevlines=True, normed=True, lw=2)
ax1.grid(True)
ax1.axhline(0, color='black', lw=2)

ax2 = fig.add_subplot(212, sharex=ax1)
ax2.acorr(approval_rating_series, usevlines=True, normed=True, lw=2)
ax2.grid(True)
ax2.axhline(0, color='black', lw=2)

plt.show()
