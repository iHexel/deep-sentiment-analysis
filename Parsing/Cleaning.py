"""Parse and Clean Tweets"""
import re
import psycopg2
import pytz
import pandas as pd
from datetime import datetime
import pandas.io.sql as psql
from pytz import timezone

# local modules
from Parsing_Functions import text_clean, findandreplace
from keys import *
from keywords_and_dicts import *

# connect to db
conn = psycopg2.connect(
    "dbname='dbsys6016' user=%s host=%s password=%s" % (user, host, password))

# pull in data
df = psql.read_sql(
    "SELECT * FROM usa_primary LIMIT 100000", conn)

# recasting
df['id'] = df['id'].apply(str)
df['text'] = df['text'].apply(str)
df['user_id'] = df['user_id'].apply(str)
df['text_lang'] = df['text_lang'].apply(str)
df['user_location'] = df['user_location'].apply(str)
df['user_handle'] = df['user_handle'].apply(str)
df['user_lang'] = df['user_lang'].apply(str)
df['source'] = df['source'].apply(str)

# filter out job bots, weather bots, geo bots, ect
df = df[~df['source'].str.contains("TweetMYJOBS")]
df = df[~df['source'].str.contains("tweetmyjobs")]
df = df[~df['text'].str.contains("Want to work in")]
df = df[~df['text'].str.contains("Can you recommend anyone for this")]
df = df[~df['text'].str.contains("CareerArc")]
df = df[~df['source'].str.contains("tweetbot")]
df = df[~df['source'].str.contains("bot")]

# filtering in specific sources
df1 = df[df['source'].str.contains("for Blackberry")]
df2 = df[df['source'].str.contains("for Android")]
df3 = df[df['source'].str.contains("for iOS")]
df4 = df[df['source'].str.contains("for iPhone")]
df5 = df[df['source'].str.contains("for Windows Phone")]
df6 = df[df['source'].str.contains("for iPad")]
df7 = df[df['source'].str.contains("for Mac")]
df8 = df[df['source'].str.contains("Twitter Web Client")]
df9 = df[df['source'].str.contains("mobile web")]
df10 = df[df['source'].str.contains("for twitter lite")]
df11 = df[df['source'].str.contains("facebook")]
df12 = df[df['source'].str.contains("TweetDeck")]
df13 = df[df['source'].str.contains("Google")]
df14 = df[df['source'].str.contains("echofon")]


# concatenate sources
dfs = [df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12, df13, df14]
dffiltered = pd.concat(dfs)

# filter by location
dffiltered = dffiltered[dffiltered['user_location'].str.contains(keywords)]

# subset location to matched keywords
dffiltered['user_location'] = dffiltered['user_location'].apply(
    lambda row: keywords.findall(row)[0].lower().strip())

# map matched keywords to a state within USA
dffiltered['user_location'] = dffiltered['user_location'].map(state_dict)

# create a timezone column based on user_location value
dffiltered['timezone'] = dffiltered['user_location'].map(tz_dict)

# convert string to datetime object
dffiltered['created_at'] = pd.to_datetime(dffiltered['created_at'])

# specify datetime object as utc timezone
dffiltered['created_at'] = dffiltered['created_at'].apply(lambda row: pytz.utc.localize(row))

# convert utc to local timezone
# eastern time zone
df_eastern = dffiltered[dffiltered['timezone'] == "Eastern"]
eastern = timezone('US/Eastern')
df_eastern = dffiltered
df_eastern['adjusted_created_at'] = df_eastern['created_at'].apply(
    lambda row: row.astimezone(eastern))

# pacific time zone
df_pacific = dffiltered[dffiltered['timezone'] == "Pacific"]
pacific = timezone('US/Pacific')
df_pacific['adjusted_created_at'] = df_pacific['created_at'].apply(
    lambda row: row.astimezone(pacific))

# mountain time zone
df_mountain = dffiltered[dffiltered['timezone'] == "Mountain"]
mountain = timezone('US/Mountain')
df_mountain['adjusted_created_at'] = df_mountain['created_at'].apply(
    lambda row: row.astimezone(mountain))

# central time zone
df_central = dffiltered[dffiltered['timezone'] == "Central"]
central = timezone('US/Central')
df_central['adjusted_created_at'] = df_central['created_at'].apply(
    lambda row: row.astimezone(central))

# concatenate the timezone dataframes
df_adjusted_filtered = pd.concat([df_central, df_eastern, df_mountain, df_pacific])

# handling @,#, and URL's
# Create empty lists for each category.
mentions = []
links = []
hashtags = []

# Iterate over the text, extracting and adding
for tweet in df_adjusted_filtered['text']:
    mentions.append(re.findall(r'@\S*', tweet))
    links.append(re.findall(r'https?://\S*', tweet))
    hashtags.append(re.findall(r'#\S*', tweet))

# Append features as a new column to the existing dataframe.
df_adjusted_filtered['hashtags'] = hashtags
df_adjusted_filtered['mentions'] = mentions
df_adjusted_filtered['links'] = links

# recasting variables
df_adjusted_filtered['text'] = df_adjusted_filtered['text'].apply(str)

# stripping non text characters ie @, # ,https://, ect
df_adjusted_filtered['cleaned_text'] = df_adjusted_filtered['text'].apply(text_clean)

# converting variations of a word with trump to just trump ie realdonaldtrump to trump
df_adjusted_filtered['cleaned_text'] = df_adjusted_filtered['cleaned_text'].apply(lambda row: findandreplace(row, "trump", "trump")

# free up memory
del df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12, df13, df14
