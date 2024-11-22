import pandas as pd
import re
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')

df = pd.read_csv('../data/raw/job_postings.csv')
stop_words = set(stopwords.words('english'))

def clean_text(text):
    text = re.sub(r'[^\w\s]', '', str(text).lower())
    return ' '.join([w for w in text.split() if w not in stop_words])

df['description'] = df['description'].apply(clean_text)
df['title'] = df['title'].apply(clean_text)
df['salary'] = df['salary'].str.extract(r'(\d+[\d,]*\d*)').replace(',', '', regex=True).astype(float, errors='ignore')
df['date'] = pd.to_datetime(df['date'].str.extract(r'(\d+ days ago|\d+ hours ago|today)')[0].replace('today', '0 days ago').str.extract(r'(\d+)')[0], errors='coerce', unit='D', origin=pd.Timestamp.now())

df.to_csv('../data/processed/job_postings_processed.csv', index=False)
print("Processed data saved to ../data/processed/job_postings_processed.csv")
