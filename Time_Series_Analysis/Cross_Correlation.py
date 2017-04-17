"""Analyzing cross correlation between time series"""
# http://statsmodels.sourceforge.net/stable/generated/statsmodels.tsa.stattools.ccf.html#statsmodels.tsa.stattools.ccf
from statsmodels.tsa.stattools import ccf
import statistics as stat
# Validation Series
from Validation_Series import valid_approval, valid_disapproval

# created series
from Deep_Sentiment_Analysis.Sentiment_Analysis.Daily_Sentiment import approval_rating_series, disapproval_rating_series

# sort index values
approval_rating_series.sort_index(inplace=True)
disapproval_rating_series.sort_index(inplace=True)

stat.mean(ccf(approval_rating_series, valid_approval))
