import matplotlib.pyplot as plt 
from task5 import netflix_df_movie_col_subset

netflix_df_movie_col_subset.plot.scatter(x='release_year', y='duration')
plt.xlabel('release_year')
plt.ylabel('Duration')
plt.title('Movie Duration By Year of Release')

plt.show()