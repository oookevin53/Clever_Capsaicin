import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
# from nltk.stem.porter import PorterStemmer
# from nltk.stem.snowball import SnowballStemmer
# from nltk.stem.wordnet import WordNetLemmatizer

class ContentRecommender(object):
    def __init__(self):
        self.df = pd.read_pickle('data_pickled.pkl')
        self.vectorizer = TfidfVectorizer()
        self.matrix = None
        self.results = {}

    # def stem(self):
    #     self.stemmer = SnowballStemmer('english',ignore_stopwords=True)

    def create_sparse(self):
        self.matrix = self.vectorizer.fit_transform(self.df.iloc[:,-1])

    def calc_similarity(self):
        cosine_similarities = cosine_similarity(self.matrix,self.matrix)
        for idx, row in self.df.iterrows():
            similar_indices = cosine_similarities[idx].argsort()[:-52:-1]
            similar_items = [(self.df['product_name'][i], '{:.2%}'.format(cosine_similarities[idx][i]), self.df['url'][i], self.df['amazon_url'][i], idx, self.df['img_url'][i]) for i in similar_indices]
            self.results[row['product_name']] = similar_items[1:]

    def _item(self,id_num):
        return self.df.loc[id_num,'product_name']

    def recommend(self,item_id, num=5):
        # print("Recommending " + str(num) + " products similar to " + self._item(item_id) + "...")
        # print("------------------------------")
        item_name = self._item(item_id)
        recs = self.results[item_name][:num]
        return recs
        # for rec in recs:
        #     print("Recommended: " + rec[1] + " (score:" + str(rec[0]) + ")")
