# -*- coding: utf-8 -*-

"""
File: plot_functions.py.
Author: Christian Vergara Retamal - Joaquín Callejón Guzmán
Email: chrvergararetamal[at]gmail[dot]com
Github: https://github.com/cvergararetamal
Description: Plot functions - Consultoria I
"""
import sys
import math
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
from os import path
import re
import nltk
import Levenshtein as lvs
from wordcloud import WordCloud, STOPWORDS
from nltk.corpus import stopwords



# Plot media de una variable
def plot_mean_custom(var, titulo = 'Valor por defecto'):
    tmp = var.dropna() # Borramos, si es que existen nulls
    plt.hist(tmp, color = 'dodgerblue')
    plt.title(titulo, size = 17)
    plt.axvline(tmp.mean(), color = 'tomato', linewidth = 2,
                linestyle = '--', label = 'Media de {}'.format(titulo))
    plt.legend()

# Plot comportamiento de pregunta 
def plot_by_quest(df, pregunta):
    aux_dict = df[pregunta].value_counts().to_dict()
    plt.bar(*zip(*aux_dict.items()))
    plt.title('Comportamiento de respuestas de {}'.format(pregunta))
    plt.show()

# Plot comportamiento de una pregunta por institución
def plot_quest_by_inst(df, pregunta, institucion):
    df_temp = df[df['institucion']==institucion]
    aux_dict = df_temp[pregunta].value_counts().to_dict()
    plt.bar(*zip(*aux_dict.items()))
    plt.title('{} en {}'.format(pregunta, institucion))

# WordCloud para comentarios de una pregunta
def wordCloud(dataframe, pregunta, palabras):
    df_temp = pd.DataFrame()
    df_temp[pregunta] = dataframe[pregunta]
    comment_words = ''
    stopwords = set(STOPWORDS)
    # Agregamos las palabras en español a las 'stopwords'
    stopwords.update(palabras)
    for val in df_temp[pregunta].values:
        val = str(val)
        tokens = val.split()
        for i in range(len(tokens)):
            tokens[i] = tokens[i].lower()
        comment_words += " ".join(tokens)+" "
    wordcloud = WordCloud(width=800, height=800, stopwords = stopwords, min_font_size= 10).generate(comment_words)
    plt.figure(figsize = (10, 10), facecolor = None) 
    plt.imshow(wordcloud, interpolation="bilinear") 
    plt.axis("off") 
    plt.tight_layout(pad = 0) 
    plt.show()

