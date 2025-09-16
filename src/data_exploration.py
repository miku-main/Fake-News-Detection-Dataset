import pandas as pd

# Load the dataset
true_df = pd.read_csv('Fake-News-Data/data/True.csv') # Real news dataset
fake_df = pd.read_csv('Fake-News-Data/data/Fake.csv') # Fake news dataset

# Adding a column to label them as real and fake
true_df['label'] = 'real'
fake_df['label'] = 'fake'

# Combining the datasets into one
df = pd.concat([true_df, fake_df], ignore_index=True)

# Check the first few rows of the combined dataset
print("First 5 rows of the combined dataset: ")
print(df.head())

# Get dataset information (column names, data types, non-null values)
print("\nDataset Info: ")
print(df.info())