# Unnest delimited list values into individual rows using Pandas explode
import pandas as pd

data = {
    'movie_id': [101, 102, 103],
    'title': ['Inception', 'Interstellar', 'The Dark Knight'],
    'genres': [
        'Action, Sci-Fi, Thriller',
        'Adventure, Drama, Sci-Fi',
        'Action, Crime, Drama',
    ],
}

df = pd.DataFrame(data)

# 1. Convert delimited genre strings into Python lists
df['genres'] = df['genres'].str.split(', ')

# 2. Unnest list elements into individual rows
df_exploded = df.explode('genres').reset_index(drop=True)

print(df_exploded)