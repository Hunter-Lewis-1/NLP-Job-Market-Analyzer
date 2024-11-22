from flask import Flask, render_template_string
import pandas as pd
import plotly.express as px

app = Flask(__name__)

@app.route('/')
def dashboard():
    df = pd.read_csv('../data/processed/skill_trends.csv')
    fig = px.line(df, x='month', y='predicted_demand', color='skills', title='Skill Demand Trends')
    fig.update_layout(
        updatemenus=[dict(
            buttons=[dict(label=s, method='update', args=[{'visible': df['skills'].eq(s)}])
                    for s in df['skills'].unique()],
            direction='down', showactive=True
        )]
    )
    graph_html = fig.to_html(full_html=False)
    return render_template_string(
        '<html><body><h1>Job Market Trends</h1>{{ graph_html|safe }}</body></html>',
        graph_html=graph_html
    )

if __name__ == '__main__':
    app.run(debug=True)
