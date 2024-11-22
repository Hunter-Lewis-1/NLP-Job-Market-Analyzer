## Methodology
Over 1,000 job postings were scraped from Indeed and processed with BERTopic to extract contextual skills (10 topics). A time-series regression (Statsmodels OLS) predicted skill demand using job frequency, months, and unemployment rates, validated against real-world trends. The dashboard was deployed via Flask and Heroku.
