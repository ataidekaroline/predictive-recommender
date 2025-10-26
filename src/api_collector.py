import requests
import pandas as pd
from typing import List, Dict

# Base URL for the Jikan API (V4 - MyAnimeList Unofficial API)
JIKAN_BASE_URL = "https://api.jikan.moe/v4"

def fetch_top_anime(limit: int = 50) -> List[Dict]:
    """
    Fetches a list of highly-rated anime from the Jikan API.
    Returns a list of dictionaries with anime data.
    """
    endpoint = f"{JIKAN_BASE_URL}/top/anime"
    # Filtering for currently airing anime is a good way to find current hype
    params = {
        "limit": limit,
        "filter": "airing",
        "sfw": True
    }
    
    print(f"Fetching top {limit} currently airing anime... - api_collector.py:21")
    try:
        response = requests.get(endpoint, params=params)
        response.raise_for_status() # Raise an HTTPError for bad responses
        data = response.json()
        
        # Return the list of anime data under the 'data' key
        return data.get('data', [])

    except requests.exceptions.RequestException as e:
        print(f"Error accessing Jikan API: {e} - api_collector.py:31")
        return []

def extract_essential_data(anime_list: List[Dict]) -> pd.DataFrame:
    """
    Extracts essential fields from the anime list into a Pandas DataFrame.
    """
    data_for_df = []
    for anime in anime_list:
        data_for_df.append({
            'mal_id': anime.get('mal_id'),
            'title': anime.get('title'),
            'score': anime.get('score'),
            'scored_by': anime.get('scored_by'),
            'genres': ", ".join([g['name'] for g in anime.get('genres', [])]), # Join genres into a single string
            'type': anime.get('type'),
            'episodes': anime.get('episodes'),
            'status': anime.get('status'),
            'airing': anime.get('airing'),
            'popularity': anime.get('popularity'),
        })
    return pd.DataFrame(data_for_df)

if __name__ == '__main__':
    top_animes_data = fetch_top_anime(limit=50)
    
    if top_animes_data:
        df_anime = extract_essential_data(top_animes_data)
        
        # Save the initial DataFrame to the 'data/' directory
        output_path = 'data/raw_anime_data.csv'
        df_anime.to_csv(output_path, index=False)
        
        print(f"\nData collected and saved to: {output_path} - api_collector.py:64")
        print("\nFirst 5 rows of the DataFrame: - api_collector.py:65")
        print(df_anime.head())
    else:
        print("Could not collect anime data. - api_collector.py:68")