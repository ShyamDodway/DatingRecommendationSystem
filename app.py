from flask import Flask, render_template, request
import pandas as pd
import numpy as np

app = Flask(__name__)

# Load your dataset
data = pd.read_csv('dating_app_dataset.csv')

# Code for match score and recommendation goes here (same as in your script)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    # Get user inputs from the form
    male_id = request.form['male_id']
    female_id = request.form['female_id']
    
    # Get the corresponding profiles
    male_profile = data[data['User ID'] == int(male_id)].iloc[0]
    female_profile = data[data['User ID'] == int(female_id)].iloc[0]

    # Calculate match score
    match_score = calculate_match_score(male_profile, female_profile)

    return f"Match Score: {match_score}"

if __name__ == '__main__':
    app.run(debug=True)
