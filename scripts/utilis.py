import pandas as pd

def save_data(df, path, name):
    df.to_csv(path+name)

from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns

IMAGES_PATH = Path().cwd()/"images"
IMAGES_PATH.mkdir(parents=True, exist_ok=True)

def save_fig(df, fig_id, tight_layout=True, fig_extension="png", resolution=300):
    
    path = IMAGES_PATH / f"{fig_id}.{fig_extension}"
    if tight_layout:
        plt.tight_layout()
    sns.boxplot(df[fig_id])
    plt.savefig(path, format=fig_extension, dpi=resolution)
    plt.show()