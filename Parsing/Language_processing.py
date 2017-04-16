"""Language Processing"""
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# local packages
from Cleaning import df_adjusted_filtered
from Parsing_Functions import process, text_clean

# Pulls in data frame created in previous sheet.
# See README for describtion of process
df = df_adjusted_filtered

# Stop Words
# english
english = stopwords.words('english')

# applying function to dataframe
df_en = df[df['user_lang'] == 'en'].reset_index(drop=True)
df_en['cleaned_text'] = df_en['cleaned_text'].apply(lambda row: process(row, english))

# free up memory
del df, df_adjusted_filtered
