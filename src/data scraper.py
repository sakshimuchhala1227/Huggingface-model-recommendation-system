import os
import pandas as pd
import requests

def fetch_model_data():
    # Hugging Face API endpoint
    url = "https://huggingface.co/api/models"
    response = requests.get(url)
    
    # Check the status code
    if response.status_code == 200:
        data = response.json()
        print(f"Received {len(data)} models from the API")  # Debug print to check how much data is fetched
        if not data:
            print("No model data received from the API")
            return

        models = []
        
        for model in data:
            models.append({
                "model_id": model.get("modelId"),
                "description": model.get("pipeline_tag", ""),
                "tags": ", ".join(model.get("tags", [])),
                "downloads": model.get("downloads", 0),
                "likes": model.get("likes", 0),
                "language": model.get("languages", "unknown")
            })
            
        # Convert models to a DataFrame
        df = pd.DataFrame(models)

        # Ensure the 'data' directory exists
        if not os.path.exists('data'):
            os.makedirs('data')

        # Save the DataFrame to CSV
        df.to_csv("data/models_data.csv", index=False)
        print("Model data saved to data/models_data.csv")
    else:
        print(f"Failed to fetch model data. Status code: {response.status_code}")

# Run the function to fetch data
if __name__ == "__main__":
    fetch_model_data()
