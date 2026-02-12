# Takes spreadhseets from a specified folder path and combines them into a single spreadsheet
# Change File Path

path = "C:\Code"
import pandas as pd
import os

def combine_spreadsheets(path):
    df_final = pd.DataFrame()
    for file in os.listdir(path):
        if '.xlsx' in file:
            df = pd.read_excel(path+"\\"+file, engine='openpyxl')
        elif '.xls' in file:
            df = pd.read_excel(path+"\\"+file)
        elif '.csv' in file:
            df = pd.read_csv(path+"\\"+file)
        else:
            continue
        df_final = pd.concat([df_final, df])
    return df_final

final_df = combine_spreadsheets(path)