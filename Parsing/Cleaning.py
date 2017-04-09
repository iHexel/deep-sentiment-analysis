"""Parse and Clean Tweets"""
import re
import pandas as pd
import pandas.io.sql as psql
import psycopg2
from mylist import loc_list

# connect to db
conn = psycopg2.connect(
    "dbname='dbsys6016' user=%s host=%s password=%s" % (user, host, password))

#pull in data
df = psql.read_sql(
    "SELECT * FROM usa_primary LIMIT 1000", conn)

# functions


def text_clean(dirtytext):
    """
    Clean text by stripping out unnecessary characters.
    Parameters
    ----------
    dirtytext : The text to be cleaned.
    """
    tmp = re.sub("'", '', dirtytext)
    tmp = re.sub(",", '', tmp)
    tmp = re.sub(r"(@\S*)|(https?://\S*)", " ", tmp)
    tmp = ' '.join(re.sub(r"(\w+:\/\/\S+)", " ", tmp).split())
    tmp = re.sub(r'[\s]+', ' ', tmp)
    tmp = re.sub(r'[^\w]', ' ', tmp)
    tmp = re.sub(' +', ' ', tmp)
    tmp = re.sub('[1|2|3|4|5|6|7|8|9|0]', '', tmp)
    tmp = re.sub('nan', ' ', tmp)
    tmp = tmp.lower()
    return tmp


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

# filtering by location
dfTest = df[df["user_location"].str.contains([mylist])]

# number of users
print(len(dffiltered['user_id']))

# handling @,#, and URL's
# Create empty lists for each category.
mentions = []
links = []
hashtags = []

# Iterate over the text, extracting and adding
for tweet in dffiltered['text']:
    mentions.append(re.findall(r'@\S*', tweet))
    links.append(re.findall(r'https?://\S*', tweet))
    hashtags.append(re.findall(r'#\S*', tweet))

# Append features as a new column to the existing dataframe.
dffiltered['hashtags'] = hashtags
dffiltered['mentions'] = mentions
dffiltered['links'] = links

# recasting variables
dffiltered['text'] = dffiltered['text'].apply(str)

# stripping non text characters ie @, # ,https://, ect
dffiltered['cleaned_text'] = dffiltered['text'].apply(text_clean)

# free up memory
del df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, d12, d13, d14
