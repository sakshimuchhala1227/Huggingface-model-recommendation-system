# import joblib
# import pandas as pd
# from sklearn.metrics.pairwise import cosine_similarity
# import numpy as np

# def recommend_models(user_prompt):
#     # Load the vectorizer, model matrix, and original models data using joblib
#     vectorizer = joblib.load("data/vectorizer.joblib")
#     model_matrix = joblib.load("data/model_matrix.joblib")
#     df = pd.read_csv("data/models_data.csv")
    
#     # Check for NaN values in the model data and handle them
#     df.fillna("", inplace=True)  # Replace NaN values with empty strings
    
#     # Vectorize the user prompt
#     prompt_vector = vectorizer.transform([user_prompt])
    
#     # Calculate similarity scores using cosine similarity
#     scores = cosine_similarity(prompt_vector, model_matrix).flatten()
    
#     # Handle NaN values in the similarity scores
#     scores = [score if not np.isnan(score) else 0 for score in scores]
    
#     # Get the top 5 recommended models based on cosine similarity
#     top_indices = np.argsort(scores)[-5:][::-1]
    
#     # Return all columns for the recommended models
#     return df.iloc[top_indices][['model_id', 'description', 'tags', 'downloads', 'likes', 'language']].to_dict(orient='records')

import joblib
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def recommend_models(user_prompt):
    # Load the vectorizer, model matrix, and original models data using joblib
    vectorizer = joblib.load("data/vectorizer.joblib")
    model_matrix = joblib.load("data/model_matrix.joblib")
    df = pd.read_csv("data/models_data.csv")
    
    # Check for NaN values in the model data and handle them
    df.fillna("", inplace=True)  # Replace NaN values with empty strings
    
    # Vectorize the user prompt
    prompt_vector = vectorizer.transform([user_prompt])
    
    # Calculate similarity scores using cosine similarity
    scores = cosine_similarity(prompt_vector, model_matrix).flatten()
    
    # Handle NaN values in the similarity scores
    scores = [score if not np.isnan(score) else 0 for score in scores]
    
    # Get the top 5 recommended models based on cosine similarity
    top_indices = np.argsort(scores)[-5:][::-1]
    
    # Select the top recommended models
    top_models = df.iloc[top_indices][['model_id', 'description', 'tags', 'downloads', 'likes', 'language']]
    
    # Convert downloads column to numeric if it's not already
    top_models['downloads'] = pd.to_numeric(top_models['downloads'], errors='coerce')
    
    # Sort the selected models by downloads in descending order
    top_models = top_models.sort_values(by='downloads', ascending=False)
    
    # Return the sorted recommended models as a dictionary
    return top_models.to_dict(orient='records')
