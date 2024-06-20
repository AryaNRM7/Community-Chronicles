# -*- coding: utf-8 -*-
"""source.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/github/SmridhVarma/Fake-News-Detection/blob/main/source.ipynb
"""

#!pip install numpy pandas scikit-learn

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC

data = pd.read_csv("fake_or_real_news.csv")
data.head(5)

"""Data encoding"""

data['fake'] = data['label'].apply(lambda x: 0 if x == 'REAL' else 1)

data.drop("Fake", axis=1, inplace=True)

data.head(5)

x,y =data['text'],data['fake']

x

y

x_train,  x_test,  y_train,  y_test =  train_test_split(x, y, test_size=0.2)

x_train

len(x_train)

len(x_test)

"""Vectorize"""

vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)
x_train_vectorized = vectorizer.fit_transform(x_train)
x_test_vectorized = vectorizer.transform(x_test)

clf = LinearSVC()
clf.fit(x_train_vectorized, y_train)

clf.score(x_test_vectorized, y_test)

len(y_test)*0.94554

"""new article no in dataset"""

with open("mytext.txt","w", encoding="utf-8") as f:
  f.write(x_test.iloc[10])

with open("mytext.txt","r",encoding="utf-8") as f:
  text=f.read()

vectorized_ip = vectorizer.transform([text])

output_array = clf.predict(vectorized_ip)
result = int(output_array[0])
if(result==1):
  print("It's fake news!")
else:
  print("It might be real!")

text

data['fake']==0

text
