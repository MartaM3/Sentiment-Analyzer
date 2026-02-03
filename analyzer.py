# Text Sentiment Analyzer


import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter
import re
import sys

# Este código contiene un dataset de ejemplo pero también puede
#importarse un CSV
if len(sys.argv) > 1:
    df = pd.read_csv(sys.argv[1])
    if 'Comments' not in df.columns:
        raise ValueError("El CSV debe contener una columna llamada 'Comments'.")
else:
    comments = [
        "I love this product, it's amazing!",
        "The app is too slow and buggy",
        "Service was okay, nothing special",
        "Fantastic experience, highly recommend",
        "Not satisfied with the quality",
        "Quick delivery and excellent support"
    ]
    df = pd.DataFrame({'Comment': comments})

#Creamos una función que 'analiza' los sentimientos
def analyze_sentiment(text):
    polarity = TextBlob(str(text)).sentiment.polarity
    if polarity > 0.1:
        return 'Positive'
    elif polarity < -0.1:
        return 'Negative'
    else:
        return 'Neutral'

df['Sentiment'] = df['Comment'].apply(analyze_sentiment)

# Resumen de la estadística
summary = df['Sentiment'].value_counts()
print("Sentiment Summary:\n", summary)

#Gráfico
colors = ['green' if x=='Positive' else 'red' if x=='Negative' else 'gray' for x in summary.index]
summary.plot(kind='bar', color=colors)
plt.title('Sentiment Distribution')
plt.ylabel('Number of Comments')
plt.show()

#Palabra mas usada según sentimiento
def get_top_words(df, sentiment, n=5):
    texts = df[df['Sentiment'] == sentiment]['Comment']
    words = " ".join(texts).lower()
    words = re.findall(r'\b\w+\b', words)
    counter = Counter(words)
    return counter.most_common(n)

for sentiment in ['Positive', 'Neutral', 'Negative']:
    print(f"Top words for {sentiment}: {get_top_words(df, sentiment)}")

#Word Cloud por sentimiento
for sentiment, colormap in zip(['Positive', 'Neutral', 'Negative'], ['Greens', 'Greys', 'Reds']):
    text = " ".join(df[df['Sentiment']==sentiment]['Comment']).lower()
    if text:
        wordcloud = WordCloud(width=800, height=400, background_color='white', colormap=colormap).generate(text)
        plt.figure(figsize=(10,5))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.title(f'{sentiment} Comments Word Cloud')
        plt.show()

