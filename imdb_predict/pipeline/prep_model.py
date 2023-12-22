import nltk 
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import re 
import pickle
import sklearn
import pandas as pd 

with open('D:\\Django projects\\Tut\\MovieReviewsEmotionDetection\\imdb_predict\\pipeline\\movie_reviews_model.pkl','rb') as file:
        lr_model = pickle.load(file)



with open('D:\\Django projects\\Tut\\MovieReviewsEmotionDetection\\imdb_predict\\pipeline\\vetorize.pkl','rb') as f :
        tf = pickle.load(f)


class pipeline():
        def __init__(self):
                self.lm = WordNetLemmatizer()
                self.stop_words =set(stopwords.words('english'))
                self.tf = tf
                self.model = lr_model

        def transform_data(self,review):
                self.review = review
                self.review = re.sub('^a-zA-Z0-9',' ',self.review)
                self.review = self.review.lower()
                self.review = self.review.split()
                self.review =[self.lm.lemmatize(x) for x in self.review if x not in self.stop_words]
                self.review = " ".join(self.review)
                return self.review 
        
        def preprocess(self,text):
                self.transformation = self.transform_data(text)
                self.transformation = self.tf.transform([self.transformation])
                return self.transformation
        
        def predict(self,preprocessed_data):
                return self.model.predict(preprocessed_data)
        
        def post_process(self,result):
                self.result = result
                return "Postive" if result ==[1] else " negative"
        
        def predict_csv_file(self,csv_file):
                file = pd.read_csv(csv_file)
                data = file.copy()
                data = data.iloc[:, 0].apply(self.transform_data)
                data = self.tf.transform(data)
                data = self.predict(data)
                result = [ self.post_process(x) for x in data]
                file['prediction']=result
                return  file.to_csv(csv_file,sep='\t', encoding='utf-8') 



'''lm = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

def transform_data(review):
        review = re.sub('^a-zA-Z0-9',' ',review)
        review = review.lower()
        review = review.split()
        review =[lm.lemmatize(x) for x in review if x not in stop_words]
        review = " ".join(review)
        return review'''




