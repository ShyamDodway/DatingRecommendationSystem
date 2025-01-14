import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
# Replace 'dating_data.csv' with the name of your CSV file
data = pd.read_csv('dating_app_dataset.csv')
print(data.head())  # Display the first few rows
# Separate data into male and female
male_profiles = data[data['Gender'] == 'Male']
female_profiles = data[data['Gender'] == 'Female']

def calculate_match_score(profile1, profile2):
    # Shared interests score (1 point per shared interest)
    interests1 = set(eval(profile1['Interests']))
    interests2 = set(eval(profile2['Interests']))
    shared_interests_score = len(interests1.intersection(interests2))

    # Age difference score (higher age difference, lower score)
    age_difference_score = max(0, 10 - abs(profile1['Age'] - profile2['Age']))

    # Swiping history score (higher swiping history, higher score)
    swiping_history_score = min(profile1['Swiping History'], profile2['Swiping History']) / 100

    # Relationship type score (1 point for matching types)
    relationship_type_score = 0
    if profile1['Looking For'] == profile2['Looking For']:
        relationship_type_score = 1

    # Total match score
    total_score = (
        shared_interests_score + age_difference_score + swiping_history_score + relationship_type_score
    )

    return total_score

# Example: Calculate match score between two profiles
profile1 = male_profiles.iloc[0]
profile2 = female_profiles.iloc[0]
match_score = calculate_match_score(profile1, profile2)
print(f"Match score between User {profile1['User ID']} and User {profile2['User ID']} : {match_score}")

def recommend_profiles(male_profiles, female_profiles):
    recommendations = []

    for _, male_profile in male_profiles.iterrows():
        best_match = None
        best_score = -1

        for _, female_profile in female_profiles.iterrows():
            score = calculate_match_score(male_profile, female_profile)

            if score > best_score:
                best_match = female_profile
                best_score = score

        recommendations.append((male_profile, best_match, best_score))

    return recommendations

# Generate recommendations
recommendations = recommend_profiles(male_profiles, female_profiles)

# Sort recommendations by match score in descending order
recommendations.sort(key=lambda x: x[2], reverse=True)

# Display the top recommendations
for idx, (male_profile, female_profile, match_score) in enumerate(recommendations[:10]):
    print(f"Recommendation {idx + 1}:")
    print(f"Male Profile (User {male_profile['User ID']}): Age {male_profile['Age']}, Interests {male_profile['Interests']}")
    print(f"Female Profile (User {female_profile['User ID']}): Age {female_profile['Age']}, Interests {female_profile['Interests']}")
    print(f"Match Score: {match_score}")
    print()