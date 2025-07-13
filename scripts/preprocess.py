import pandas as pd

def merge_data(combined_data):
    combined_data["train_data"]['data'] = 'train'
    combined_data["test_data"]['data'] = 'test'

    return pd.concat([combined_data["train_data"], combined_data["test_data"]], axis=0) 

def impute_null(combined_data):
    combined_data["geo"]["geo_score"] = combined_data["geo"]["geo_score"].fillna(combined_data["geo"]["geo_score"].median())
    combined_data["qset"]["qsets_normalized_tat"] = combined_data["qset"]["qsets_normalized_tat"].fillna(combined_data["qset"]["qsets_normalized_tat"].median())


def groupby_df(combined_data):
    combined_data["geo"] = combined_data["geo"].groupby('id').mean()
    combined_data["qset"] = combined_data["qset"].groupby('id').mean()
    combined_data["instance"] = combined_data["instance"].groupby('id').mean()

def split(all_data):
    return (all_data[all_data["data"]=='train'], all_data[all_data["data"]=='test'])

def clean(train_data, test_data):
    return train_data.drop(['id', 'Group', 'Target', 'data'], axis=1), train_data['Target'], test_data.drop(['id', 'Group', 'Target', 'data'], axis = 1)

