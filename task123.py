years = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
durations = [103, 101, 99, 100, 100, 95, 95, 96, 93, 90]
#create a dictionary with the two lists.  task 1
movie_dict = {"years":[2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020], "durations":[103, 101, 99, 100, 100, 95, 95, 96, 93, 90]}

print(movie_dict)

import pandas as pd 
#create as a dataframe from the dictionary
durations_df = pd.DataFrame(movie_dict)
print(durations_df)

#import matplotlib.pyplot under its usual alias and create a figure
import matplotlib.pyplot as plt
#draw a line plot release_years and durations
plt.plot(years, durations, marker='o')
#create a title
plt.title('Movie length by year')
plt.xlabel('years')
plt.ylabel('duration (minutes)')
plt.show()



