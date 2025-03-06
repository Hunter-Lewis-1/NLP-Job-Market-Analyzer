# Multi-Modal Job Market Trend Analyzer
Analyzes real job market trends using NLP and regression, with a live dashboard.
## Setup
Install dependencies: `pip install -r requirements.txt`
## Usage
1. Scrape data: `python scripts/scrape_jobs.py`
2. Preprocess: `python scripts/preprocess_data.py`
3. Extract skills: `python models/extract_skills.py`
4. Predict trends: `python models/regression_model.py`
5. Run locally: `python dashboard/app.py`
## Results
View results locally at `localhost:5000`.
