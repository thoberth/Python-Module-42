import seaborn as sns
import pandas as pd
from typing import List
import matplotlib.pyplot as plt

class MyPlotLib:
    @staticmethod
    def histogram(data: pd.DataFrame, features: List[str]):
        if verify_arg(data, features):
            fig, axs = plt.subplots(ncols=len(features))
            for i, to_print in enumerate(features):
                sns.histplot(data=data, x=to_print, ax=axs[i])
            plt.show()

    @staticmethod
    def density(data: pd.DataFrame, features: List[str]):
        if verify_arg(data, features):
            fig, axs = plt.subplots(ncols=len(features))
            for i, to_print in enumerate(features):
                sns.kdeplot(data=data, x=to_print, ax=axs[i])
            plt.show()

    @staticmethod
    def pair_plot(data: pd.DataFrame, features: List[str]):
        if verify_arg(data, features):
            sns.pairplot(data=data, vars=features)
            plt.show()

    @staticmethod
    def box_plot(data: pd.DataFrame, features: List[str]):
        if verify_arg(data, features):
            fig, axs = plt.subplots(ncols=len(features))
            for i, to_print in enumerate(features):
                sns.boxplot(data=data, x=to_print, ax=axs[i])
            plt.show()

def verify_arg(data: pd.DataFrame, features: List[str]) -> bool:
    good_col = df.select_dtypes(include=['float', 'int']).columns
    for col in features:
        if col not in good_col:
            print(f'Error in parameters, {col} is a bad argument')
            return False
    return True


if __name__ =="__main__":
    df = pd.read_csv("../athlete_events.csv")
    mpl = MyPlotLib()
    mpl.box_plot(df, ['Weight', 'Height', 'Name'])
    mpl.histogram(df, ['Weight', 'Height'])
    mpl.density(df, ['Weight', 'Height'])
    mpl.pair_plot(df, ['Weight', 'Height'])
    mpl.box_plot(df, ['Weight', 'Height'])
