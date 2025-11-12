import pandas as pd
import numpy as np
import os
import sys

# Add the project root to sys.path to import modules if necessary
# This part is crucial for running stand-alone scripts inside src/
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def generate_synthetic_ratings(df_anime: pd.DataFrame, num_users: int = 200, min_ratings: int = 5) -> pd.DataFrame:
    """
    Generates simulated user ratings based on anime's official score and calculated hype.
    Users are simulated to rate popular/hyped items slightly higher.
    
    Args:
        df_anime (pd.DataFrame): DataFrame containing anime metadata and 'hype_score'.
        num_users (int): The number of synthetic users to create.
        min_ratings (int): Minimum number of items each user rates.
        
    Returns:
        pd.DataFrame: A DataFrame with columns ['user_id', 'mal_id', 'rating'].
    """
    all_ratings = []
    # Ensure mal_id is an integer for the recommender system
    anime_ids = df_anime['mal_id'].astype(int).tolist()
    
    # Normalize scores for better combination in simulation
    df_anime['normalized_score'] = df_anime['score'] / 10.0
    
    # Hype Score (-1 to 1) adjusted to be 0 to 1 for weighted simulation: (x + 1) / 2
    df_anime['adjusted_hype'] = (df_anime['hype_score'] + 1) / 2 
    
    # Map for quick lookup during simulation
    anime_map = df_anime.set_index('mal_id')[['normalized_score', 'adjusted_hype']].T.to_dict()

    print(f"Generating synthetic ratings for {num_users} users...")
    
    for user_id in range(1, num_users + 1):
        
        # Randomly determine how many items this user rates (max 15% of the total list)
        num_rated_items = np.random.randint(min_ratings, len(anime_ids) * 0.15) 
        rated_anime_ids = np.random.choice(anime_ids, num_rated_items, replace=False)
        
        for mal_id in rated_anime_ids:
            
            # Base rating influenced by official score (60%) and adjusted hype (40%)
            base_rating_influence = (anime_map[mal_id]['normalized_score'] * 0.6) + \
                                    (anime_map[mal_id]['adjusted_hype'] * 0.4)
            
            # Convert back to 1-10 scale and introduce random noise (simulating individual taste)
            rating = np.clip(
                np.round(base_rating_influence * 10 + np.random.normal(0, 1.5)), 
                1, 10
            )
            
            all_ratings.append({
                'user_id': user_id,
                'mal_id': int(mal_id),
                'rating': int(rating)
            })
    
    return pd.DataFrame(all_ratings)

    
if __name__ == '__main__':
    PROCESSED_DATA_FILE = 'data/processed_anime_data.csv'
    RATING_DATA_FILE = 'data/synthetic_user_ratings.csv'
    
    # Ensure the data directory exists
    data_dir = os.path.dirname(RATING_DATA_FILE)
    if data_dir and not os.path.exists(data_dir):
        os.makedirs(data_dir)
        
    try:
        if not os.path.exists(PROCESSED_DATA_FILE):
            print(f"Error: Required file '{PROCESSED_DATA_FILE}' not found. Run hype_detector.py first!")
        else:
            df_processed = pd.read_csv(PROCESSED_DATA_FILE)
            
            df_ratings = generate_synthetic_ratings(df_processed, num_users=200)
            
            # Save synthetic user ratings
            df_ratings.to_csv(RATING_DATA_FILE, index=False)
            print(f"\n✅ Synthetic ratings generated and saved to: {RATING_DATA_FILE}")
            print("\nSample Ratings:")
            print(df_ratings.head())
            
    except Exception as e:
        print(f"A critical error occurred during processing: {e}")