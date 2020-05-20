# -*- coding: utf-8 -*-
"""
Created on Wed May 20 18:48:33 2020

@author: lokopobit
"""

# Load external libreries
import os
import pandas as pd

def join_csvs(folder_path):
    shows_paths = os.listdir(folder_path)
    for show_path in shows_paths:
        show_folder = os.listdir(os.path.join(folder_path, show_path))
        show_csvs = [file for file in show_folder if file[-4:] == '.csv']
        total_df = pd.DataFrame()
        for show_csv in show_csvs:
            df = pd.read_csv(os.path.join(os.path.join(folder_path, show_path),show_csv))
            total_df = pd.concat([total_df, df])  
        new_name = show_path + '_total.csv'
        total_df.to_csv(os.path.join(os.path.join(folder_path, show_path),new_name))

