import nltk 
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import re 
import pickle
import sklearn

lm = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

def transform_data(review):
        review = re.sub('^a-zA-Z0-9',' ',review)
        review = review.lower()
        review = review.split()
        review =[lm.lemmatize(x) for x in review if x not in stop_words]
        review = " ".join(review)
        return review


with open('D:\\Django projects\\Tut\\MovieReviewsEmotionDetection\\MovieReviewsEmotionDetection\\model\\movie_reviews_model.pkl','rb') as file:
        lr_model = pickle.load(file)



with open('D:\\Django projects\\Tut\\MovieReviewsEmotionDetection\\MovieReviewsEmotionDetection\\model\\vetorize.pkl','rb') as f :
        tf = pickle.load(f)


