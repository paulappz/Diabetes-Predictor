# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
folder = "C:\\Users\\Paul\\Downloads\\diabetes_data\\"
import pandas as pd
diabetes = pd.read_csv(folder + 'pima-indians-diabetes.csv')
diabetes.head()
