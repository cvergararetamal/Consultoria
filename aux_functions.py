# -*- coding: utf-8 -*-

"""
File: plot_functions.py.
Author: Christian Vergara Retamal - Joaquín Callejón Guzmán
Email: chrvergararetamal[at]gmail[dot]com
Github: https://github.com/cvergararetamal
Description: Auxiliar functions - Consultoria I
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

        
# Función para separar preguntas
def splitAnswers(df, pregunta):
    index = df.columns.get_loc(pregunta)
    new_col1 = df[pregunta].str.split(';').str[0]
    new_col2 = df[pregunta].str.split(';').str[1]
    df.insert(loc = index, column = '{}.1'.format(pregunta), value = new_col1)
    df.insert(loc = index+1, column = '{}.2'.format(pregunta), value = new_col2)
    df.drop([pregunta], axis = 1, inplace = True)
    
