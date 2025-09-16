import pandas as pd
from preprocessing import clean_dataframe

# Load datasets
true_df = pd.read_csv('Fake-News-Data/data/True.csv')
fake_df = pd.read_csv('Fake-News-Data/data/Fake.csv')

# Label datasets
true_df['label'] = 'real'
fake_df['label'] = 'fake'

# Combine datasets
df = pd.concat([true_df, fake_df], ignore_index=True)

# Preprocess the text
df = clean_dataframe(df)

# Show original vs cleaned text
print(df[['text', 'cleaned_text', 'label']].head())