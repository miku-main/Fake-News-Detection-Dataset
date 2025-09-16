import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Downloading NLTK data (run this once, it'll save resources on the computer)
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('punkt_tab')   # Add this to download the missing resource

# Function to preprocess text
def preprocess_text(text):
    """
    Clean and preprocess news article text.
    Steps:
    1. Convert all to lowercase
    2. Remove any punctuation
    3. Tokenize into words
    4. Remove stopwords
    5. Join tokens back into a string
    """
    
    # Lowercase
    text = text.lower()
    
    # Remove punctuation
    text = ''.join([char for char in text if char not in string.punctuation])
    
    # Tokenize
    tokens = word_tokenize(text)
    
    # Remove Stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    
    # Rejoin tokens
    return ' '.join(tokens)

def clean_dataframe(df):
    # Apply preprocessing to the 'text' column of the dataset.
    # Adds a new column 'cleaned_text'.
    df['cleaned_text'] = df ['text'].apply(preprocess_text)
    return df