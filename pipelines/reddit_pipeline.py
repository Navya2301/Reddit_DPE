
from utils.constants import SECRET, CLIENT_ID
from etls.reddit_etl import connect_reddit

def reddit_pipleine(ile_name:str, subreddit:str, time_filtery='da',limit= None):
    # we use this function to do the following things
    # 1. connection to reddit instance
    instance = connect_reddit(CLIENT_ID, SECRET, 'Airscholar Agent') # constants that we get from utils <- config.conf
    # 2. Extraction
    posts = extract_posts(instance, subreddit, time_filter, limit)
    # 3. Transformation
    # 4. Loading to CSV