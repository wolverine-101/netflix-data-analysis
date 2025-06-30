# First we import data manipulation and visualization libraries
# Then we read the Netflix dataset and print the first few rows
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('netflix_titles.csv')
print(df.head())

# Check basic info
print("\nDataset Info:")
print(df.info())

# Check for null values
print("\nMissing Values:")
print(df.isnull().sum())

# Drop rows where 'type' or 'title' is missing (essential fields)
df.dropna(subset=['type', 'title'], inplace=True)

# Fill missing 'country' and 'rating' values with placeholders
df['country'] = df['country'].fillna('Unknown')
df['rating'] = df['rating'].fillna('Not Rated')

sns.countplot(data=df, x='type', hue='type', palette='Set2', legend=False)


# Convert 'date_added' to datetime
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

# Create new column for release year
df['release_year'] = df['release_year'].astype('Int64')  # in case there are nulls


# Type distribution
print("\nType Distribution:")
print(df['type'].value_counts())

# Plot: Movie vs TV Show
sns.countplot(data=df, x='type', palette='Set2')
plt.title('Count of Movies vs TV Shows on Netflix')
plt.xlabel('Type')
plt.ylabel('Count')
plt.tight_layout()
plt.show()


df['year_added'] = df['date_added'].dt.year

plt.figure(figsize=(10, 5))
df['year_added'].value_counts().sort_index().plot(kind='bar', color='coral')
plt.title('Content Added to Netflix Over the Years')
plt.xlabel('Year Added')
plt.ylabel('Number of Titles')
plt.tight_layout()
plt.show()



from collections import Counter

genre_list = df['listed_in'].dropna().str.split(', ')
flat_genres = [genre for sublist in genre_list for genre in sublist]
top_genres = Counter(flat_genres).most_common(10)

genres, counts = zip(*top_genres)

plt.figure(figsize=(10, 5))
sns.barplot(x=list(counts), y=list(genres), palette='viridis')
plt.title('Top 10 Netflix Genres')
plt.xlabel('Count')
plt.tight_layout()
plt.show()
