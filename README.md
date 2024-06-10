<div align="center">
  <br>
  <h1>📊 Sentiment Analysis Using SpaCy</h1>
  <strong>Beginner Natural Language Processing (NLP) Project</strong>
</div>
<br>

This project performs sentiment analysis on customer reviews for Amazon products. It leverages natural language processing (NLP)
techniques to preprocess the text data and determine the sentiment of the reviews. The primary goal is to classify reviews as positive,
negative, or neutral, thereby providing valuable insights into customer opinions.

**Dataset:** [Amazon Product Reviews By Kaggle](https://www.kaggle.com/datasets/datafiniti/consumer-reviews-of-amazon-products)

### Modules
![Spacy Version](https://img.shields.io/badge/spacy-v3.7.2-blue)
![Pandas Version](https://img.shields.io/badge/pandas-v2.2.2-blue)
![Conda Version](https://img.shields.io/badge/conda-v24.5.0-blue)
![Python Version](https://img.shields.io/badge/python-v3.12.2-blue)
![SpacyTextBlob Version](https://img.shields.io/badge/spacytextblob-v4.0.0-blue)


### Modules and Functions

- **pandas:** For data manipulation and analysis.
- **spacy:** For advanced NLP tasks.
- **spacytextblob:** For sentiment analysis.

#### Custom Function: `preprocess_text`

This function performs several preprocessing tasks:
- Converts text to lowercase.
- Removes punctuation, numbers, and named entities.
- Retains important stop words crucial for sentiment analysis.
- Lemmatizes tokens to their base forms.

```python
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
```
  
<img width="768" alt="Screenshot 2024-06-10 at 23 54 35" src="https://github.com/EroldGjoka/Sentiment_Analysis/assets/162522371/e5a24abc-3cf2-4591-a160-824de64b4ddd">
