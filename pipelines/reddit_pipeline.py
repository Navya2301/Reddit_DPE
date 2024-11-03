
from utils.constants import SECRET, CLIENT_ID, OUTPUT_PATH
from etls.reddit_etl import connect_reddit, extract_posts, transform_data, load_data_to_csv

import pandas as pd

def reddit_pipeline(file_name:str, subreddit:str, time_filter='day',limit= None):
    # we use this function to do the following things
    # 1. connection to reddit instance
    instance = connect_reddit(CLIENT_ID, SECRET, 'Airscholar Agent') # constants that we get from utils <- config.conf
    # 2. Extraction
    posts = extract_posts(instance, subreddit, time_filter, limit)
    post_df = pd.DataFrame(posts)
    
    # 3. Transformation
    post_df = transform_data(post_df)


    # 4. Loading to CSV
    file_path = f'{OUTPUT_PATH}/{file_name}.csv' #mentioning output file name
    load_data_to_csv(post_df, file_path)