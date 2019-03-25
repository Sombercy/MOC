#! /usr/bin/env python
# -*- coding: utf-8 -*-
from scipy.spatial.distance import cdist
import numpy as np
import re

lst = list()
words = list()
with open('sentences.txt') as f:
    for line in f:
        # ! /usr/bin/env python
        # -*- coding: utf-8 -*-
        line1 = line.strip()# без табуляций
        line1 = line1.lower()# понижение регистра
        lst.append(re.split('[^a-z]', line1)) #только слова
for line in lst:
    for word in line:
        if len(word) > 0:
            words.append(word) # убираем пустые строки
#print(len(lst))
words = set(words) # без повторяющихся слов
#print (len(words))

kw = {}
i = 0
for word in words:
    kw [i] = word # ключ (индекс) - слово
    i += 1

A = np.empty((len(lst), len(kw))) # пустой массив кол-во предложений на кол-во слов
#print(A.shape)
for i in range(len(lst)):
    for j in range(len(kw)):
        A[i][j] = lst[i].count(kw[j]) # сколько раз в i-том предложении встречается j-ое слово
print(cdist(A[0:1], A[1:], metric='cosine')) # косинусное растояние от 0-го предложения до остальных




