# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
# import re
# import nltk
# from nltk.corpus import stopwords
# from nltk.stem import PorterStemmer
# from nltk.stem import WordNetLemmatizer
# from nltk.tokenize import word_tokenize
# from nltk.tokenize import sent_tokenize
# from wordcloud import WordCloud
# from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score
# from sklearn.metrics import confusion_matrix
# from sklearn.metrics import classification_report
# from sklearn.metrics import make_scorer, roc_curve, roc_auc_score
# from sklearn.metrics import precision_recall_fscore_support as score
# from sklearn.metrics.pairwise import cosine_similarity
# from sklearn.ensemble import RandomForestClassifier
# import pickle

# similarity = pickle.load(open('similarity.pkl', 'rb'))

# def remove_tags(text):
#     remove = re.compile(r'')
#     return re.sub(remove, '', text)

# def special_char(text):
#     reviews = ''
#     for x in text:
#         if x.isalnum():
#             reviews = reviews + x
#         else:
#             reviews = reviews + ' '
#     return reviews

# def convert_lower(text):
#     return text.lower()

# def remove_stopwords(text):
#     stop_words = set(stopwords.words('english'))
#     words = word_tokenize(text)
#     return [x for x in words if x not in stop_words]

# def lemmatize_word(text):
#     wordnet = WordNetLemmatizer()
#     return " ".join([wordnet.lemmatize(word) for word in text])

# def recommend(blog, new):
#     index = new[new['headline'] == blog].index[0]
# #     print(index)
#     try:
#         distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
#         for i in distances[1:15]:
#             print(new.iloc[i[0]].headline)
#     except:print("Error")

# def main():

#     dataset = pd.read_csv("C:\\Users\\Sahil\\Desktop\\Hackathon\\Rubix-23-2-Team-Jod\\team_jod\\blog\\NewsCategorizer.csv")
#     dataset = dataset.drop(['links'],axis="columns")
#     target_category = dataset['Category'].unique()
#     dataset['CategoryId'] = dataset['Category'].factorize()[0]
#     category = dataset[['Category', 'CategoryId']].drop_duplicates().sort_values('CategoryId')
#     dataset = dataset.dropna()
#     text = dataset["Text"]
#     category = dataset['Category']
#     pd.options.mode.chained_assignment = None

#     dataset['Text'] = dataset['Text'].apply(remove_tags)
#     dataset['Text'] = dataset['Text'].apply(special_char)
#     dataset['Text'] = dataset['Text'].apply(convert_lower)
#     dataset['Text'] = dataset['Text'].apply(remove_stopwords)
#     dataset['Text'] = dataset['Text'].apply(lemmatize_word)

#     dataset['keywords'] = dataset['keywords'].apply(lambda x:x.split('-'))
#     dataset['Text'] = dataset['Text'].apply(lambda x:x.split())
#     dataset['Category'] = dataset['Category'].apply(lambda x:x.split())

#     dataset['tags'] = dataset['Text'] + dataset['keywords'] + dataset['Category']
#     new = dataset.drop(columns=['Text','keywords', 'links'])
#     new['tags'] = new['tags'].apply(lambda x: " ".join(x))
#     new['Category'] = new['Category'].apply(lambda x: " ".join(x))

    


import pickle
import pandas as pd


def recommend(blog):
    similarity = pickle.load(open("C:\\Users\\Sahil A\\Desktop\\Rubix Hackathon\\Rubix-23-2-Team-Jod\\team_jod\\data\\similarity.pkl", 'rb'))
    new = pd.read_csv("C:\\Users\\Sahil A\\Desktop\\Rubix Hackathon\\Rubix-23-2-Team-Jod\\team_jod\\data\\UpdatedCSV.csv")
    try:
        recommender_list = []
        index = new[new['headline'] == blog].index[0]

    
        distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
        for i in distances[1:5]:
            recommender_list.append(new.iloc[i[0]].headline)

    except:print("Error")
        
    return recommender_list
        
    

