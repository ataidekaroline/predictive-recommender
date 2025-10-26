import os
from dotenv import load_dotenv

# load all the files from .env to python (os.environ)
load_dotenv() 

# now the keys are read from environment variables
MAL_CLIENT_ID = os.getenv("MAL_CLIENT_ID")
MAL_CLIENT_SECRET = os.getenv("MAL_CLIENT_SECRET")

REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
REDDIT_CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")
REDDIT_USER_AGENT = os.getenv("REDDIT_USER_AGENT")


if not MAL_CLIENT_ID or not MAL_CLIENT_SECRET:
    print("WARNING: MAL_CLIENT_ID or MAL_CLIENT_SECRET not found in environment. Check your .env file!")