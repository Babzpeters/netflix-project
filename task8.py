from task5 import netflix_df_movie_col_subset

color = []


for index, row in netflix_movie_col_subset.iterrows() :
    if row['genre'] == 'children':
        color.append('red')
    elif row['genre'] == 'Documentary':
        color.append('blue')
    elif row['genre'] == 'stand-up':
        color.append('green')
    else:
        color.append('black')

print(color[:10])        

    
        
    