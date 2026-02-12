# Requires pandas and numpy

import pandas as pd
import numpy as np

df1 = pd.read_excel("2nd_excel.xlsx", engine="openpyxl")
df2 = pd.read_excel("1st_excel.xlsx", engine="openpyxl")

# rows in df2 not in df1
df_extra = df2.iloc[-(len(df2) - len(df1)):]

# rows in df2 that are in df1
df2_min = df2.iloc[0:min(len(df2), len(df1))]
df1_min = df1.iloc[0:min(len(df2), len(df1))]
comparison_values = df2_min.values == df1_min.values
rows,cols=np.where(comparison_values == False)
df_comparison = df2_min.copy()

for item in zip(rows, cols):
    df_comparison.iloc[item[0], item[1]] = '{} --> {}'.format(df1_min.iloc[item[0], item[1]], df2_min.iloc[item[0], item[1]])

    df_comparison