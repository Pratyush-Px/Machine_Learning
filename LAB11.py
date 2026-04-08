# Basic NLP preprocessing example

import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

# Sample text
text = "Natural Language Processing is amazing! It helps computers understand human language."

# Step 1: Convert to lowercase
text = text.lower()

# Step 2: Remove punctuation
text = text.translate(str.maketrans('', '', string.punctuation))

# Step 3: Tokenization
tokens = word_tokenize(text)

# Step 4: Remove stopwords
stop_words = set(stopwords.words('english'))
filtered_words = []

for word in tokens:
    if word not in stop_words:
        filtered_words.append(word)

# Step 5: Stemming
ps = PorterStemmer()
stemmed_words = []

for word in filtered_words:
    stemmed_words.append(ps.stem(word))

# Output results
print("Original Tokens:", tokens)
print("After Stopword Removal:", filtered_words)
print("After Stemming:", stemmed_words)