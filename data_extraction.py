import pandas as pd
import json
import requests
from google.cloud import storage


def data_extraction_from_api():
    url= "https://api.themoviedb.org/3/movie/top_rated?api_key=e6c4eb1bc805e2cf433b4f5365690487&language=en-US&page=1"

    try:
        response = requests.get(url)
        results=response.json()['results']   
        return results
    except requests.exceptions.RequestException as e:
        print("Failure reason:",e)
    
def create_dataframe():
    df=pd.DataFrame(data_extraction_from_api())
    return df


create_dataframe()