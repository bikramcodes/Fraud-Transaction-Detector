import seaborn as sns
import pandas as pd

def boxplots(df, col):
    sns.boxplot(df[col])
    save_fig(col)
    plt.show()


