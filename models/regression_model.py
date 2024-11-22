import pandas as pd
import statsmodels.formula.api as smf

# Load job data
df = pd.read_csv('../data/processed/job_postings_processed.csv')
skills_df = pd.read_csv('../data/processed/skills_extracted.csv')
df = df.merge(skills_df[['job_id', 'skills']], left_index=True, right_on='job_id')

# Aggregate by month and skill
df['month'] = df['date'].dt.to_period('M').astype(str)
trend_data = df.groupby(['month', 'skills']).size().reset_index(name='frequency')

# Add mock external data (unemployment rate as proxy)
unemployment = pd.DataFrame({
    'month': ['2024-01', '2024-02', '2024-03', '2024-04', '2024-05', '2024-06'],
    'unemployment_rate': [3.7, 3.8, 3.9, 3.8, 3.7, 3.6]
})
trend_data = trend_data.merge(unemployment, on='month', how='left').fillna(method='ffill')

# Fit time-series regression
model = smf.ols('frequency ~ C(skills) + unemployment_rate + month', data=trend_data).fit()
trend_data['predicted_demand'] = model.predict(trend_data)

# Save results
trend_data.to_csv('../data/processed/skill_trends.csv', index=False)
print("Trends saved to ../data/processed/skill_trends.csv")
