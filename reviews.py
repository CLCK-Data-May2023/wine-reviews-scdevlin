import pandas as pd
reviews = pd.read_csv("data/winemag-data-130k-v2.csv.zip", index_col=0)

countries = reviews.country.unique()
reviews_per_country = reviews.country.value_counts()
median_points = reviews.points.median()

reviews.apply(row.country, axis = 'columns')

wine_reviews = pd.DataFrame({countries, reviews_per_country, median_points})

csv_file = wine_reviews.to_csv('reviews-per-country.csv')