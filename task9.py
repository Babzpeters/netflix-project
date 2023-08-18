from task5 import netflix_df_movie_col_subset
from task8 import color
import matplotlib.pyplot as plt

netflix_movie_col_subset.plot.scatter(x='release_year', y='durtion', c=color, alpha=0.8)
plt.xlabel('release year')
plt.xlabel('Duration(mins')
plt.title('movie duration by year of release')

plt.show()