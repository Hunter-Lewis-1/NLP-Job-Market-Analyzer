from bertopic import BERTopic
import pandas as pd

df = pd.read_csv('../data/processed/job_postings_processed.csv')
docs = df['description'].tolist()

topic_model = BERTopic(nr_topics=10, min_topic_size=10, embedding_model='all-MiniLM-L6-v2')
topics, _ = topic_model.fit_transform(docs)
skills = [','.join([word for word, _ in topic_model.get_topic(t)[:3]]) if t != -1 else 'misc' for t in topics]

df['skills'] = skills
df[['title', 'skills']].to_csv('../data/processed/skills_extracted.csv', index_label='job_id')
print("Skills extracted and saved to ../data/processed/skills_extracted.csv")
