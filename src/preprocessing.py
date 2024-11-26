# import pandas as pd
# from sklearn.feature_extraction.text import TfidfVectorizer
# import pickle

# def load_and_preprocess_data():
#     # Load data
#     df = pd.read_csv("data/models_data.csv")
    
#     # Combine description and tags columns and handle NaN values
#     text_data = (df['description'].fillna('') + " " + df['tags'].fillna('')).values
#     # Vectorize with TF-IDF
#     vectorizer = TfidfVectorizer(stop_words='english')
#     model_matrix = vectorizer.fit_transform(text_data)
    
#     # Save vectorizer and model matrix
#     with open("data/vectorizer.pkl", "wb") as vec_file, open("data/model_matrix.pkl", "wb") as mat_file:
#         pickle.dump(vectorizer, vec_file)
#         pickle.dump(model_matrix, mat_file)
    
#     print("Data preprocessing complete and saved")

# # Run the preprocessing step
# if __name__ == "__main__":
#     load_and_preprocess_data()
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib

def load_and_preprocess_data():
    # Load data
    df = pd.read_csv("data/models_data.csv")
    
    # Combine description and tags columns and handle NaN values
    text_data = (df['description'].fillna('') + " " + df['tags'].fillna('')).values
    
    # Vectorize with TF-IDF
    vectorizer = TfidfVectorizer(stop_words='english')
    model_matrix = vectorizer.fit_transform(text_data)
    
    # Save vectorizer, model matrix, and original data as joblib files
    joblib.dump(vectorizer, "data/vectorizer.joblib")
    joblib.dump(model_matrix, "data/model_matrix.joblib")
    joblib.dump(df.to_dict(orient="records"), "data/models_data.joblib")
    
    print("Data preprocessing complete and saved")

# Run the preprocessing step
if __name__ == "__main__":
    load_and_preprocess_data()

