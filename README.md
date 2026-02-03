# Text Sentiment Analyzer

This project is a **comment sentiment analyzer** developed in Python.  
It classifies comments as **Positive, Negative, or Neutral**, generates statistics and visualizations, and creates word clouds for each sentiment category.

---

## Features

- Automatic classification of comments into Positive, Negative, and Neutral.
- Bar chart showing the distribution of sentiments.
- Word cloud for each category.
- Works with any CSV file containing a `Comment` column.
- Includes a **sample dataset** for testing.

> ⚠️ Important note: The tool **may not accurately detect neutral comments**, as automatic sentiment analysis has limitations with ambiguous or nuanced texts.

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/Text-Sentiment-Analyzer.git
cd Text-Sentiment-Analyzer
```
2. Install required libraries:
```bash
pip install -r requirements.txt
```
3. Download TextBlob support data:
```bash
python -m textblob.download_corpora
```
## Usage 
1. Run the script with your own CSV
```bash
python analyzer.py comments.csv
```
2. Or run it with the included sample dataset:
```bash
python analyzer.py
```
3. Output includes:
a) Table of comments with their sentiment
b) Bar chart of sentiment distribution
c) Top words by category
d) Word cloud by category
