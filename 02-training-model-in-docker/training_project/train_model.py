import mlflow.xgboost
import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split


def train_test_split_pandas(df, t_size=0.33, r_tate=42):
    train_dataset = df.iloc[:, :-1]
    target_dataset = df.iloc[:, -1]
    return train_test_split(train_dataset, target_dataset, test_size=t_size, random_state=r_tate)


if __name__ == "__main__":
    THRESHOLD = 0.5

    mlflow.xgboost.autolog()
    with mlflow.start_run(run_name="train_model") as run:
        mlflow.set_tag("mlflow.runName", "train_model")

        pandas_df = pd.read_csv("data/training/data.csv", header=None)

        X_train, X_test, y_train, y_test = train_test_split_pandas(pandas_df)

        train_data = xgb.DMatrix(X_train, label=y_train)
        test_data = xgb.DMatrix(X_test)

        model = xgb.train(dtrain=train_data, params={})

        y_predictions = model.predict(test_data)
        y_binary_predictions = [1 if y_p > THRESHOLD else 0. for y_p in y_predictions]

        test_prediction_results = pd.DataFrame(data={'y_pred': y_binary_predictions, 'y_test': y_test})

        test_prediction_results.to_csv("data/predictions/test_predictions.csv")

