import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Ensure 'images' directory exists
if not os.path.exists('images'):
    os.makedirs('images')

# Load the dataset
data = pd.read_csv("API_SP.POP.TOTL_DS2_en_csv_v2_19373/API_SP.POP.TOTL_DS2_en_csv_v2_19373.csv", skiprows=4)

# Set the year
year = '2022'

# Filter the data for the selected year
data_year = data[['Country Name', year]].dropna()

# Get the top 10 most populous countries
top10 = data_year.sort_values(by=year, ascending=False).head(10)

# Plot the data
plt.figure(figsize=(10,6))
sns.barplot(x=year, y='Country Name', data=top10, palette='viridis')

# Set the title and labels
plt.title(f'Top 10 Most Populous Countries in {year}')
plt.xlabel('Population')
plt.ylabel('Country')

# Save the plot as an image in the 'images' directory
plt.tight_layout()  # Adjust layout
plt.savefig('population_barplot_2022.png')  # Save the plot

# Show the plot
plt.show()
