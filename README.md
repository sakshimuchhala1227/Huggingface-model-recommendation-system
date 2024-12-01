<h1 align="center" id="title">Hugging Face Model Recommendation System</h1>

<p id="description">This project is a Hugging Face Model Recommendation System designed to assist users in discovering the most suitable models based on their task descriptions. The system analyzes user-provided prompts and recommends models from the Hugging Face library by leveraging machine learning techniques for natural language processing and similarity scoring.</p>

  
  
<h2>🧐 Features</h2>

Here're some of the project's best features:

*   User-Friendly Interface: A Streamlit-powered frontend for entering task descriptions and viewing model recommendations.
*   Efficient Backend: FastAPI-based backend for handling requests and providing recommendations in real-time.
*   Advanced Text Analysis: Utilizes TF-IDF (Term Frequency-Inverse Document Frequency) for feature extraction from text.
*   Accurate Recommendations: Employs cosine similarity to match user prompts with models' descriptions and tags.
*   Optimized Data Processing: Built with joblib for efficient handling of preprocessed data and model matrix storage.

<h2>📊 Workflow</h2>
    <ol>
        <li><b>Data Scraping:</b> A scraping script fetches metadata of Hugging Face models, such as descriptions, tags, downloads, likes, and language.</li>
        <li><b>Data Preprocessing:</b> 
            <ul>
                <li>Combines model descriptions and tags into a single text representation.</li>
                <li>Applies TF-IDF vectorization to generate feature matrices for model matching.</li>
            </ul>
        </li>
        <li><b>User Input Handling:</b> Accepts a task description as input via the Streamlit interface and converts the user prompt into a TF-IDF vector.</li>
        <li><b>Similarity Scoring:</b> Calculates cosine similarity between the user input vector and preprocessed model data, ranks and returns the top matching models.</li>
        <li><b>Results Display:</b> Presents recommended models along with metadata such as description, tags, downloads, likes, and language.</li>
    </ol>

    
<h2>🛠️ Installation Steps:</h2>

<p>1. Clone the repository</p>

```
git clone https://github.com/sakshimuchhala1227/Huggingface-model-recommendation-system.git
```

<p>2. Install dependencies</p>

```
pip install -r requirements.txt  
```

<p>3. Scrape the data</p>

```
python src/data_scraper.py  
```

<p>4. Preprocess the data</p>

```
python src/preprocessing.py  
```

<p>5. Start the FastAPI server</p>

```
uvicorn src.api:app --reload  
```

<p>6. Launch the Streamlit app</p>

```
cd  streamlit run frontend/app.py  
```

  
  
<h2>💻 Built with</h2>

Technologies used in the project:

*   Frontend: Streamlit
*   Backend: FastAPI
*   Machine Learning: Scikit-learn (TF-IDF and cosine similarity)
*   Data Handling: Pandas joblib
*   Deployment Ready: Docker-compatible architecture for scalability


 <h2>📂 File Structure</h2>
    <pre>
project-root/  
│  
├── src/  
│   ├── data/  
│   │   ├── models_data.csv          # Dataset containing model metadata  
│   │   ├── vectorizer.joblib        # Saved TF-IDF vectorizer  
│   │   └── model_matrix.joblib      # Preprocessed model matrix  
│   │  
│   ├── data_scraper.py              # Data scraping script  
│   ├── preprocessing.py             # Data preprocessing and TF-IDF vectorization  
│   ├── recommendation.py            # Recommendation logic  
│   └── api.py                       # FastAPI backend implementation  
│  
├── frontend/  
│   └── app.py                       # Streamlit app for user interaction  
│  
├── requirements.txt                 # Project dependencies  
└── README.md                        # Project documentation  
    </pre>
