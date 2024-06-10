''' --------- Sentiment Analysis With SpaCy ----------
Our sentiment analysis project explores an Amazon dataset
with the aim of determining whether a given review is positive or negative.'''


import spacy
import pandas as pd

from spacytextblob.spacytextblob import SpacyTextBlob


# Load Dataset
df = pd.read_csv("amazon_product_reviews.csv")


df.info()


shape = df.shape
print(f'''---\n\n\nTotal number of rows: {shape[0]}
Total number of columns: {shape[1]}\n\n\n---''')


# Initialise the train pipeline
nlp = spacy.load("en_core_web_sm")


# Subset text reviews from dataset
reviews_data = df["reviews.text"]


# Identify  & remove missing values
missing_reviews = reviews_data.isna().sum()
print(f"Missing text reviews: {missing_reviews}\n\n\n---")

reviews_data = reviews_data.dropna()
print(f"Missing text reviews: {reviews_data.isna().sum()}\n\n\n---")


''' ------------- Keep Important Stop Words ---------------
Before removing any stop words or applying
any preprocessing techniques, we first need to ensure that we keep
some important stop words, such as 'not', 'good', 'bad', 'poor',
and many others. These words are crucial because
removing them can alter the sentiment of the text. '''


# Remove important stop words from nlp vocabulary
important_words = {
    'not', 'good', 'bad', 'excellent', 'poor', 'like', 'dislike',
    'love', 'hate', 'recommend', 'worst', 'best', 'amazing', 'terrible',
    "n‘t", "n’t"
}


for word in important_words:
    if word in nlp.Defaults.stop_words:
        nlp.Defaults.stop_words.remove(word)
        nlp.vocab[word].is_stop = False


''' ------------- Text Preprocessing Function ----------------
This fuction, will perform the necessary text preprocessing in our text.'''


# Text preprocessing function
def preprocess(text):

    if isinstance(text, str):
        text = text.replace("n't", "not")

        doc = nlp(text)

        no_stop_words = []
        for token in doc:
            if token.is_stop or token.is_punct or token.ent_type_ or not token.is_alpha:
                continue
            no_stop_words.append(token.lemma_)
        return " ".join(no_stop_words)
    return text


# Apply text preprocessing in text reviews
reviews_data = reviews_data.apply(preprocess)


# Add textblob pipeline
nlp.add_pipe("spacytextblob")


'''--------------- Sentiment Analysis Function -----------------
This function will take a dataset or a list of sentences,
along with the index you want to process, and perform
sentiment analysis.
'''


# Sentiment Analysis Function
def sentiment_analysis(dataset, index_num):
    doc = nlp(dataset.iloc[index_num])

    sentiment = doc._.blob.sentiment

    print(f"*{"*":\\>100}\n\n")
    print(f"Review {index_num+1}:\t\t{dataset.iloc[index_num]}")
    print(f"Sentiment Score:\t{sentiment}\n\n")
    print(f"*{"*":/>100}")


# Perform sentiment analysis in reviews_data on row 2, 11, and 101.
sentiment_analysis(reviews_data, 1)
sentiment_analysis(reviews_data, 10)
sentiment_analysis(reviews_data, 100)
