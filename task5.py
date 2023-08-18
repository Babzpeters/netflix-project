from task4 import netflix_df

netflix_df_movie_only = netflix_df.loc[netflix_df['type'].isin(['movie'])]

netflix_df_movie_col_subset = netflix_df_movie_only[['title', 'country', 'genre', 'release_year', 'duration']]
print(netflix_df_movie_col_subset.head(5))

