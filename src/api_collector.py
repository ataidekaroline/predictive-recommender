import requests
import pandas as pd
from typing import List, Dict, Optional
from config import MAL_CLIENT_ID # Import only the client ID for ranking access

# MAL V2 API Endpoint
MAL_API_BASE_URL = "https://api.myanimelist.net/v2"

# Define the fields we need from the MAL API response
# These fields are required for the Recommender and Hype Detector
FIELDS_TO_FETCH = [
    "id", "title", "main_picture", "mean", "num_list_users", 
    "num_scoring_users", "start_date", "genres", "num_episodes", "status"
]

def fetch_top_anime_mal(limit: int = 50) -> Optional[List[Dict]]:
    """
    Fetches the top ranked anime list directly from the official MyAnimeList API V2.
    Uses the MAL_CLIENT_ID for authentication.
    """
    endpoint = f"{MAL_API_BASE_URL}/anime/ranking"
    
    # Request parameters for the top-rated list
    params = {
        "ranking_type": "all",  # Use 'all' for overall ranking
        "limit": limit,
        "fields": ",".join(FIELDS_TO_FETCH)
    }
    
    # MAL V2 requires the Client ID in the header for public endpoints
    headers = {
        "X-MAL-CLIENT-ID": MAL_CLIENT_ID
    }
    
    print(f"Fetching top {limit} anime from MyAnimeList Official API...")
    try:
        response = requests.get(endpoint, params=params, headers=headers)
        response.raise_for_status() # Raise an HTTPError for bad responses (e.g., 401, 403, 404)
        data = response.json()
        
        # The ranking data is nested under the 'data' key
        # Each item is structured as {'node': {...anime_data...}}
        return [item['node'] for item in data.get('data', [])]

    except requests.exceptions.RequestException as e:
        print(f"Error accessing MAL API: {response.status_code} {response.reason}")
        print(f"Full URL tried: {response.url}")
        print(f"Details: {e}")
        return None

def extract_essential_data(anime_list: List[Dict]) -> pd.DataFrame:
    """
    Extracts and standardizes essential fields from the MAL response.
    """
    data_for_df = []
    for anime in anime_list:
        data_for_df.append({
            'mal_id': anime.get('id'),
            'title': anime.get('title'),
            'score': anime.get('mean'), # Mean is the average score
            'scored_by': anime.get('num_scoring_users'), 
            'genres': ", ".join([g['name'] for g in anime.get('genres', [])]), 
            'type': anime.get('media_type'), # MAL uses 'media_type'
            'episodes': anime.get('num_episodes'),
            'status': anime.get('status'),
            'popularity': anime.get('num_list_users'), # Use 'num_list_users' as a proxy for popularity
        })
    return pd.DataFrame(data_for_df)

if __name__ == '__main__':
    top_animes_data = fetch_top_anime_mal(limit=50)
    
    if top_animes_data:
        df_anime = extract_essential_data(top_animes_data)
        
        # Save the initial DataFrame to the 'data/' directory
        output_path = 'data/raw_anime_data.csv'
        df_anime.to_csv(output_path, index=False)
        
        print(f"\n✅ Data collected successfully and saved to: {output_path}")
        print("\nFirst 5 rows of the DataFrame:")
        print(df_anime.head())
    else:
        print("❌ Could not collect anime data.")