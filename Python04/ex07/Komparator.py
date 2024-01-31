import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from typing import List

class Komparator:
    def __init__(self, df: pd.DataFrame):
        self.df = df
        self.num_col = df.select_dtypes(include=['float', 'int']).columns

    def compare_box_plots(self, categorical_var: str, numerical_var: str):
        if categorical_var not in self.df.columns or numerical_var not in self.df.columns or numerical_var not in self.num_col:
            print('Error with arg')
            return
        sns.catplot(self.df, x=numerical_var, y=categorical_var, kind='box')
        plt.show()

    def density(self, categorical_var: str, numerical_var: str):
        if categorical_var not in self.df.columns or numerical_var not in self.df.columns or numerical_var not in self.num_col:
            print('Error with arg')
            return
        sns.kdeplot(self.df, x=numerical_var, hue=categorical_var)
        plt.show()

    def compare_histograms(self, categorical_var: str, numerical_var: str):
        if categorical_var not in self.df.columns or numerical_var not in self.df.columns or numerical_var not in self.num_col:
            print('Error with arg')
            return
        df_copy = self.df.dropna(subset=[categorical_var]).copy()
        col = list(set(df_copy[categorical_var].tolist()))
        fig, axs = plt.subplots(ncols=len(col))
        for i, to_print in enumerate(col):
            df_to_print = self.df[self.df[categorical_var] == to_print].copy()
            sns.histplot(df_to_print, x=numerical_var, y=categorical_var, ax=axs[i])
        plt.show()

if __name__ == "__main__":
    k = Komparator(pd.read_csv('../athlete_events.csv'))
    k.compare_box_plots('Sex', 'Height')
    k.density('Medal', 'Age')
    k.compare_histograms('Medal', 'Height')
