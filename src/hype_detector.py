import pandas as pd
import praw
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import time
import math
import os
import sys

# Add the project root to sys.path to import 'config'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import config 

# --- 1. INITIALIZATION ---

try:
    # Attempt to initialize the Reddit API (PRAW)
    reddit = praw.Reddit(
        client_id=config.REDDIT_CLIENT_ID,
        client_secret=config.REDDIT_CLIENT_SECRET,
        user_agent=config.REDDIT_USER_AGENT
    )
    # Check if Reddit credentials were loaded
    if not config.REDDIT_CLIENT_ID:
        raise ValueError("Reddit credentials not found. Please check your .env file.")
        
except Exception as e:
    print(f"❌ ERROR: Failed to initialize PRAW. Check your keys in .env. Details: {e}")
    reddit = None 
    
# Initialize VADER Sentiment Analyzer
# CORREÇÃO: Usar um bloco try/except simples focado na LookupError.
try:
    sia = SentimentIntensityAnalyzer()
except LookupError:
    print("VADER lexicon not found. Downloading...")
    # Realiza o download do lexicon e tenta inicializar novamente
    nltk.download('vader_lexicon')
    sia = SentimentIntensityAnalyzer()
    
# --- 2. CORE LOGIC ---

def analyze_sentiment(text: str) -> float:
    """Calculates the VADER compound score for a given text."""
    return sia.polarity_scores(text)['compound']

def calculate_hype_score(anime_title: str, max_posts: int = 5) -> float:
    """
    Collects social data and calculates a composite Hype Score (Sentiment + Volume).
    """
    if reddit is None:
        return 0.0 

    # Search query focused on the anime title and related discussions
    search_query = f'"{anime_title}" (discussion OR review)'
    
    comments_data = []
    total_post_score = 0
    
    # Search 'hot' posts in general anime subreddits
    for submission in reddit.subreddit('anime+manga').search(search_query, sort='hot', limit=max_posts):
        total_post_score += submission.score
        
        try:
            submission.comments.replace_more(limit=100) 
            
            for comment in submission.comments.list():
                if isinstance(comment, praw.models.Comment) and len(comment.body) > 10:
                    comments_data.append({
                        'text': comment.body,
                        'score': comment.score, 
                    })
        except Exception:
            continue 
    
    if not comments_data and total_post_score < 10:
        return 0.0 

    df_comments = pd.DataFrame(comments_data)
    
    # 1. Sentiment Component: Average sentiment of all collected comments
    df_comments['sentiment'] = df_comments['text'].apply(analyze_sentiment)
    avg_sentiment = df_comments['sentiment'].mean() if not df_comments.empty else 0.0
    
    # 2. Volume Component: Total comments + Total score of all related posts
    total_volume = len(df_comments) + total_post_score
    
    # Apply Logarithm to volume for scaling
    scaled_volume = math.log10(1 + total_volume) / 5.0
    
    # --- Weighted Hype Score Formula ---
    hype_score = (avg_sentiment * 0.6) + (scaled_volume * 0.4)
    
    return max(-1.0, min(1.0, hype_score)) 

def process_hype_data(input_path: str, output_path: str):
    """
    Reads base data, calculates Hype Score for each anime, and saves the processed data.
    """
    df_anime = pd.read_csv(input_path)
    hype_scores = []
    
    print(f"\nStarting Hype Score calculation for {len(df_anime)} anime...")
    
    for index, row in df_anime.iterrows():
        title = row['title']
        
        # Respect Reddit API rate limits with a 2-second sleep
        time.sleep(2) 
        
        try:
            score = calculate_hype_score(title)
            hype_scores.append(score)
            print(f"[{index+1}/{len(df_anime)}] Hype Score for '{title}': {score:.4f}")
        except Exception as e:
            print(f"Failed to calculate hype for {title}. Error: {e}")
            hype_scores.append(0.0)

    df_anime['hype_score'] = hype_scores
    
    # Ensure the 'data' directory exists before saving
    data_dir = os.path.dirname(output_path)
    if data_dir and not os.path.exists(data_dir):
        os.makedirs(data_dir)
        
    df_anime.to_csv(output_path, index=False)
    print(f"\n--- HYPE ANALYSIS COMPLETE ---")
    print(f"Processed data saved to: {output_path}")


if __name__ == '__main__':
    INPUT_FILE = 'data/raw_anime_data.csv'
    OUTPUT_FILE = 'data/processed_anime_data.csv'
    
    # Check if the base data file exists before proceeding
    if not os.path.exists(INPUT_FILE):
        print(f"Error: Input file '{INPUT_FILE}' not found. Run api_collector.py first!")
    else:
        process_hype_data(INPUT_FILE, OUTPUT_FILE)