import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from tqdm.notebook import tqdm
nltk.download('vader_lexicon')


def sentiment(inputs):
    sia = SentimentIntensityAnalyzer()

    ss=sia.polarity_scores(inputs)
    comment_type = ""
    if((ss['neg'])< (ss['pos'])):
        comment_type = "Positive :)"
    elif((ss['pos'])< (ss['neg'])):
        comment_type = "Negative :("
    return comment_type
    