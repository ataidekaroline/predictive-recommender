import pandas as pd
import os
import joblib # Used for saving Hype data mapping (Python object)

# Import necessary components from the surprise library
try:
    from surprise import Reader, Dataset, SVD
    from surprise import dump
except ImportError:
    print("CRITICAL ERROR: 'scikit-surprise' not found.")
    print("Please run: pip install scikit-surprise")
    sys.exit(1)

# Import system modules for path management
import sys
# Add project root to sys.path to ensure module imports work if needed
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# --- CONFIGURATION ---
RATING_DATA_FILE = 'data/synthetic_user_ratings.csv'
PROCESSED_DATA_FILE = 'data/processed_anime_data.csv'
MODEL_PATH = 'models/collaborative_filter.model' # Path for the Surprise model file
HYPE_DATA_MAPPING_PATH = 'models/hype_data_mapping.pkl' # Path for the Hype data mapping file

def train_and_save_model():
    """
    Loads ratings, trains the SVD Collaborative Filtering model, 
    and saves the model and the Hype Score data mapping for the Flask API.
    """
    if not os.path.exists(RATING_DATA_FILE) or not os.path.exists(PROCESSED_DATA_FILE):
        print("ERROR: Required data files (ratings or processed anime) not found.")
        print("Ensure you have run 'data_processing.py' and 'hype_detector.py' first.")
        return

    # 1. Load Data
    df_ratings = pd.read_csv(RATING_DATA_FILE)
    df_anime_processed = pd.read_csv(PROCESSED_DATA_FILE)
    
    # Ensure 'mal_id' is integer for Surprise
    df_ratings['mal_id'] = df_ratings['mal_id'].astype(int)

    # 2. Prepare Data for Surprise
    # Define the rating scale (1 to 10)
    reader = Reader(rating_scale=(1, 10)) 
    
    # Load the DataFrame into a Surprise Dataset
    data = Dataset.load_from_df(df_ratings[['user_id', 'mal_id', 'rating']], reader)
    
    # Build the full training set
    trainset = data.build_full_trainset()

    # 3. Train the Model
    print("Starting SVD Collaborative Filtering model training...")
    # SVD: Singular Value Decomposition (a common matrix factorization technique)
    algo = SVD(n_epochs=20, lr_all=0.005, reg_all=0.1, random_state=42)
    algo.fit(trainset)
    print("Training complete.")

    # 4. Save the Collaborative Filtering Model (using surprise's dump function)
    os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)
    dump.dump(MODEL_PATH, algo=algo)
    print(f"✅ Collaborative Filtering model saved to: {MODEL_PATH}")

    # 5. Create and Save Hype Data Mapping (Crucial for Hybrid Logic)
    # The Flask app needs quick access to Hype Score and Mean Score by mal_id
    hype_mapping = df_anime_processed.set_index('mal_id')[['score', 'hype_score', 'title', 'genres']].to_dict('index')
    
    # Save the mapping using joblib (better for dictionaries/Python objects)
    joblib.dump(hype_mapping, HYPE_DATA_MAPPING_PATH)
    print(f"✅ Hype/Score data mapping saved to: {HYPE_DATA_MAPPING_PATH}")


if __name__ == '__main__':
    train_and_save_model()