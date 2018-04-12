import pickle
import pandas as pd
import numpy as np
import gzip
from io import BytesIO
import boto3

# client = boto3.client('s3') #low-level functional API

# read in the sims and dataframe
# obj = client.get_object(Bucket='podcastorage', Key='pod_sims.npy')
# sims = np.load(BytesIO(obj['Body'].read()))
f = gzip.GzipFile('sparse_sims.npy.gz', "r")
sims = np.load(f)
pods = pd.read_pickle('pod_df.gz', compression='gzip')

# create a function to take in user-entered amounts and apply the model
def podcast_recommendations(podcast, num_recs=30, sims=sims):
    # load pods dataframe
    df = pods

    # get podcast index
    pod_index = df.index.get_loc(df.loc[df.Podcast == podcast].iloc[0].name)

    # return a message
    recs = df.iloc[np.argsort(sims[pod_index]),0][-(num_recs+1):-1][::-1]

    return np.random.choice(list(recs))
