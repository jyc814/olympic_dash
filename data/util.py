import pandas as pd 
import os


def get_data(PATH):
    df = pd.read_csv(PATH)
    df.dropna(inplace=True)
    medals = df.groupby(["Team", "Medal"])[["Medal"]].count()
    medals.rename(columns={"Medal":"Medal_Count"}, inplace=True)
    medals.sort_values(by="Medal_Count", ascending=False, inplace=True)
    medals.reset_index(inplace=True)
    medals = medals.iloc[:20]
    
    return medals