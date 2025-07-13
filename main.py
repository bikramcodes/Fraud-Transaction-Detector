from scripts.data_loader import load_csv
from scripts.preprocess import merge_data, impute_null, groupby_df, split, clean
from scripts.utilis import save_data, save_fig
from scripts.train_lgr import prepare, train, predict, report, save_model
import pandas as pd



def main():

    # Creating dictionary of empty Data Frames
    combined_data = {"geo" : 0,
                    "instance" : 0,
                    "lambdawts" : 0,
                    "qset" : 0,
                    "test_data" : 0,
                    "train_data" : 0}
    
    
    # Loading data
    for data_frame in combined_data.keys():
        combined_data[data_frame] = load_csv(rf"data\raw\{data_frame}.csv")
    
    # Merging train and test data
    all_data = merge_data(combined_data)

    # Adding all_data to the dictionary 
    combined_data['all_data'] = all_data

    # Handling null values
    impute_null(combined_data)

    # Grouping by
    groupby_df(combined_data)

    # Merging all the data
    all_data = pd.merge(all_data, combined_data["geo"], on='id', how = 'left')
    all_data = pd.merge(all_data, combined_data["instance"] , on='id', how = 'left')
    all_data = pd.merge(all_data, combined_data["qset"] , on='id', how = 'left')
    all_data = pd.merge(all_data, combined_data["lambdawts"], on='Group', how = 'left')

    #Splitting data
    train_data, test_data = split(all_data)

    #Cleaning data
    X, y, test_data = clean(train_data, test_data)

    # Saving data
    save_data(X, r"data/processed/", r"X.csv")
    save_data(y, r"data/processed/", r"y.csv")
    save_data(test_data, r"data/processed/", r"test_data.csv")

    # Saving and displaying the boxplots
    for i in list(X.select_dtypes(exclude = ['object']).columns):
        if i != 'Per3':
            save_fig(X, i)
        else:
            break

    # Model building
    X_train, X_test, y_train, y_test = prepare(X, y)
    trained_model = train(X_train, y_train)
    pred_train = predict(trained_model, X_train)
    pred_test = predict(trained_model, X_test)

    # Reports 
    report(y_train, pred_train)
    report(y_test, pred_test)

    # Saving the model
    save_model(trained_model, "models/", "logistics_regression")

    #Print Thanks
    print()
    print()
    print()
    print("Thanks")

if __name__ == "__main__":
    main()