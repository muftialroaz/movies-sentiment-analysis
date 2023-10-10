import numpy as np
import pandas as pd
import os

df = pd.read_csv('E:\PROJECT\Python-Pro\movies-sentiment-analysis\movie.csv', sep=',')
df.head

## Data cleaning

text = df['text']
# 1 Lowering case: Mengubah teks menjadi huruf kecil untuk konsistensi dalam analisis
text = text.str.lower()
text

# import re

# 2 Menghapus karakter khusus kecuali huruf dan angka
text = text.str.replace(r'[^a-zA-Z0-9\s]', '', regex=True)
text

# 3 Tokenisasi Memisahkan teks menjadi unit-unit yang lebih kecil seperti kata-kata atau frasa.
import nltk
# nltk.download('punkt')
from nltk.tokenize import word_tokenize

text = text.apply(lambda x: word_tokenize(x))
text

# 4 Menghapus Stopwords Menghapus kata-kata umum yang tidak memberikan informasi penting dalam analisis.
from nltk.corpus import stopwords
# nltk.download('stopwords')
stop_words = set(stopwords.words('english'))  # Menggunakan kamus stop words Bahasa Inggris
text = text.apply(lambda x: [word for word in x if word not in stop_words])
text

# 5 Lematisasi atau Stemming: Mengubah kata-kata ke bentuk dasar mereka untuk mengurangi variasi kata yang sama
from nltk.stem import WordNetLemmatizer
# nltk.download('wordnet')
lemmatizer = WordNetLemmatizer()
text = text.apply(lambda x: [lemmatizer.lemmatize(word) for word in x])
text

# 6 Menghapus Kata Pendek: Menghapus kata-kata dengan panjang karakter yang terlalu pendek yang cenderung tidak memiliki makna.

min_length = 3  # Menentukan panjang minimum kata yang diizinkan
text = text.apply(lambda x: [word for word in x if len(word) >= min_length])
text

# 7 Menggabungkan Kembali Teks: Menggabungkan kembali unit-unit teks yang telah dibersihkan menjadi teks yang telah diolah sepenuhnya.
text = text.apply(lambda x: ' '.join(x))
print(text)

# #Bag-of-Word
# from sklearn.feature_extraction.text import CountVectorizer

# # Inisialisasi CountVectorizer
# vectorizer = CountVectorizer()

# # Memproses teks dan membangun vocabulary
# X = vectorizer.fit_transform(text)

# # Membuat DataFrame dari hasil Bag-of-Words
# df_bow = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names_out())

# # Menggabungkan hasil Bag-of-Words dengan DataFrame asli
# df_final = pd.concat([df, df_bow], axis=1)

# print(df_final)