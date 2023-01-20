import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from sklearn.feature_extraction.text import CountVectorizer
import pickle


def remove_tags(text):
    remove = re.compile(r'')
    return re.sub(remove, '', text)

def special_char(text):
    reviews = ''
    for x in text:
        if x.isalnum():
            reviews = reviews + x
        else:
            reviews = reviews + ' '
    return reviews

def convert_lower(text):
    return text.lower()

def remove_stopwords(text):
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text)
    return [x for x in words if x not in stop_words]

def lemmatize_word(text):
    wordnet = WordNetLemmatizer()
    return " ".join([wordnet.lemmatize(word) for word in text])



def categorize_blog(text_content):

    dataset = pd.read_csv("C:\\Users\\Sahil A\\Desktop\\Rubix Hackathon\\Rubix-23-2-Team-Jod\\team_jod\\NewsCategorizer.csv")
    dataset = dataset.drop(['links'],axis="columns")
    target_category = dataset['Category'].unique()
    dataset['CategoryId'] = dataset['Category'].factorize()[0]
    category = dataset[['Category', 'CategoryId']].drop_duplicates().sort_values('CategoryId')
    dataset = dataset.dropna()
    text = dataset["Text"]
    category = dataset['Category']
    pd.options.mode.chained_assignment = None

    dataset['Text'] = dataset['Text'].apply(remove_tags)
    dataset['Text'] = dataset['Text'].apply(special_char)
    dataset['Text'] = dataset['Text'].apply(convert_lower)
    dataset['Text'] = dataset['Text'].apply(remove_stopwords)
    dataset['Text'] = dataset['Text'].apply(lemmatize_word)

    x = dataset['Text']
    y = dataset['CategoryId']

    x = np.array(dataset.iloc[:,1:4].values)
    y = np.array(dataset.CategoryId.values)
    cv = CountVectorizer(max_features = 2000)
    x = cv.fit_transform(dataset.Text).toarray()
    
    contents = cv.transform([str(text_content)])    
    model = pickle.load(open("C:\\Users\\Sahil A\\Desktop\\Rubix Hackathon\\Rubix-23-2-Team-Jod\\team_jod\\data\\blogcat.model", "rb"))
    yy = model.predict(contents)
    result = ""
    if yy == [0]:
        result = "Sports"
    elif yy == [1]:
        result = "Entertainment"
    elif yy == [2]:
        result = "Politics"
    print(result)

    return result