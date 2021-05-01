!pip install textblob
!pip install git+https://github.com/JustAnotherArchivist/snscrape.git


import snscrape.modules.twitter as sntwitter
import pandas
from textblob import TextBlob
from nltk.corpus import stopwords
import re

# Creating list to append tweet data to
tweets_list2 = []

# Using TwitterSearchScraper to scrape data and append tweets to list
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('Dextenza since:2021-01-01 until:2021-03-30').get_items()):
    if i>500:
        break
    tweets_list2.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
    
# Creating a dataframe from the tweets list above
tweets_df2 = pd.DataFrame(tweets_list2, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])

from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer

tweets_df2['Text'].str.split()



pattern = re.compile(r"(MD|Dr|PhD)")
tweets_df2 = pd.DataFrame(tweets_list2, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
stop = stopwords.words('english')
tweets_df2['Doc'] = tweets_df2['Username'].str.contains(pattern,re.IGNORECASE)
MD_df = tweets_df2[tweets_df2['Doc'] == True]

MD_df['Text_no_stop'] = MD_df['Text'].apply(lambda x: ' '.join([word for word in x.split() if word not in stop]) )

def getSubjectivity(text):
   return TextBlob(text).sentiment.subjectivity
  
 #Create a function to get the polarity
def getPolarity(text):
   return TextBlob(text).sentiment.polarity
# for i in MD_df['tok']:
#     MD_df['tok'] = ' '.join(i)
MD_df['subjectivity'] = MD_df['Text_no_stop'].apply(lambda x: getSubjectivity(x))
MD_df['polarity'] = MD_df['Text_no_stop'].apply(lambda x: getPolarity(x))

MD_df.head()
