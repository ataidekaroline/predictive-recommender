import requests
import pandas as pd
from typing import List, Dict, Optional
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# FIX: Imports the entire config module, which is in the project root
import config 

# MAL V2 API Endpoint
MAL_API_BASE_URL = "https://api.myanimelist.net/v2"

# Define the fields we need from the MAL API response
FIELDS_TO_FETCH = [
    "id", "title", "main_picture", "mean", "num_list_users", 
    "num_scoring_users", "start_date", "genres", "num_episodes", "status"
]

def fetch_top_anime_mal(limit: int = 50) -> Optional[List[Dict]]:
    """
    Fetches the top ranked anime list directly from the official MyAnimeList API V2.
    Uses the MAL_CLIENT_ID for authentication.
    """
    
    # Add security check (Using config prefix)
    if not config.MAL_CLIENT_ID:
        print("ERROR: MAL_CLIENT_ID is not loaded. Please check config.py and .env file.")
        return None
        
    endpoint = f"{MAL_API_BASE_URL}/anime/ranking"
    
    params = {
        "ranking_type": "all",  # Use 'all' for overall ranking
        "limit": limit,
        "fields": ",".join(FIELDS_TO_FETCH)
    }
    
    headers = {
        # The individual key is passed here
        "X-MAL-CLIENT-ID": config.MAL_CLIENT_ID 
    }
    
    print(f"Fetching top {limit} anime from MyAnimeList Official API...")
    try:
        response = requests.get(endpoint, params=params, headers=headers)
        response.raise_for_status() 
        data = response.json()
        
        return [item['node'] for item in data.get('data', [])]

    except requests.exceptions.RequestException as e:
        print(f"Error accessing MAL API: {response.status_code} {response.reason}")
        print(f"Full URL tried: {response.url}")
        print(f"Details: {e}")
        return None

def extract_essential_data(anime_list: List[Dict]) -> pd.DataFrame:
    
    data_for_df = []
    for anime in anime_list:
        data_for_df.append({
            'mal_id': anime.get('id'),
            'title': anime.get('title'),
            'score': anime.get('mean'), 
            'scored_by': anime.get('num_scoring_users'), 
            'genres': ", ".join([g['name'] for g in anime.get('genres', [])]), 
            'type': anime.get('media_type'), 
            'episodes': anime.get('num_episodes'),
            'status': anime.get('status'),
            'popularity': anime.get('num_list_users'), 
        })
    return pd.DataFrame(data_for_df)

if __name__ == '__main__':
    top_animes_data = fetch_top_anime_mal(limit=50)
    
    if top_animes_data:
        df_anime = extract_essential_data(top_animes_data)
        
        output_path = 'data/raw_anime_data.csv'
        
        # Ensure the 'data' directory exists before attempting to save
        data_dir = os.path.dirname(output_path)
        if data_dir and not os.path.exists(data_dir):
            os.makedirs(data_dir)
        # ---------------------------------------------
        
        df_anime.to_csv(output_path, index=False)
        
        print(f"\n✅ Data collected successfully and saved to: {output_path}")
        print("\nFirst 5 rows of the DataFrame:")
        print(df_anime.head())
    else:
        print("❌ Could not collect anime data.")