import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
import nltk
from nltk.corpus import stopwords
datafile=os.path.join('my_aa','labeledTrainData.tsv')
df=pd.read_csv(datafile,sep='\t',escapechar='\\')
print('Number of reviews:{}'.format(len(df)))
df.head()
def clean_text(text):
    text=BeautifulSoup(text,'html.parser').get_text()
    text=re.sub('[^a-zA-Z]',' ',text)
    words=text.lower().split()
    words=[w for w in words if w not in eng_stopwords]
    return ' '.join(words)
df['clean_review']=df.review.apply(clean_text)
df.head()
vectorizer=CountVectorizer(max_features=5000)
train_data_features=vectorizer.fit_transform(df.clean_review).toarray()
train_data_features.shape
import logging
from gensim.models.word2vec import Word2Vec
from gensim.models import word2vec
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
sentences = word2vec.LineSentence("text8.txt")
num_features = 300    # Word vector dimensionality
min_word_count = 40   # Minimum word count
num_workers = 4       # Number of threads to run in parallel
context = 10          # Context window size
downsampling = 1e-3   # Downsample setting for frequent words
model = Word2Vec(sentences, workers=num_workers, \
                 size=num_features, min_count = min_word_count, \
                 window = context, sample = downsampling)
# If you don't plan to train the model any further, calling 
# init_sims will make the model much more memory-efficient.
model.init_sims(replace=True)
# It can be helpful to create a meaningful model name and 
# save the model for later use. You can load it later using Word2Vec.load()
model.save(os.path.join('p_models')
forest=RandomForestClassifier(n_estimators=100)
forest=forest.fit(train_data_features,df.sentiment)
del df 
del train_data_features
datafile=os.path.join('my_aa','p_testData.tsv')
df=pd.read_csv(datafile,sep='\t',escapechar='\\')
print('Number of reviews:{}'.format(len(df)))
df['clean_review']=df.review.apply(clean_text)
df.head()
test_data_features=vectorizer.transform(df.clean_review).toarray()
test_data_features.shape
result=forest.predict(test_data_features)
output=pd.DataFrame({'id':df.id,'sentiment':result})
output.head()
output.to_csv(os.path.join('my_aa','model.csv'),index=False)
del df
el test_data_features
