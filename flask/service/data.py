import pandas as pd
import datetime, time
import os
import random
import numpy as np
import scipy.sparse as sp
import json

def initial_data():
    # movielens
    df_users = pd.read_csv("../Data/movielens/users.dat", sep = "::", header=None, engine='python',
                   names=["UserID", "Gender", "Age", "Occupation", "Zip-code"])
    df_movies = pd.read_csv("../Data/movielens/movies.dat", sep = "::", header=None, engine='python',
                   names=["MovieID", "Title", "Genres"], encoding='ISO-8859-1')
    df_ratings = pd.read_csv("../Data/movielens/ratings.dat", sep="::", header=None, engine='python',
                          names=["UserID", "MovieID", "Rating", "Timestamp"])

    # urls
    df_posters = pd.read_csv("data/movie_poster.csv", names=["MovieID", "PosterUrl"])

    # ALL
    df = pd.merge(df_movies, df_ratings, on="MovieID")
    df = pd.merge(df, df_users, on="UserID")
    df = pd.merge(df, df_posters, on="MovieID")

    return df,df_users,df_movies,df_ratings,df_posters

# root_dir = '/Users/asteriachiang/Documents/5001_Foundations_of_Data_Analytics/model/' # please set the root_dir to the folder which stores the model and the file
# df = pd.read_csv(root_dir + "MovieLens_IMDB.csv", index_col = 0)
# print(len(df['MovieID'].unique()))
#
# df_ML_movies, df_users, df_movies, df_ratings, df_posters = initial_data()
# print(len(df_ML_movies['MovieID'].unique()))
