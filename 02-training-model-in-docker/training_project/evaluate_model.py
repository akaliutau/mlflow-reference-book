import mlflow
import pandas as pd
from sklearn.metrics import \
    accuracy_score, \
    average_precision_score, \
    f1_score, \
    jaccard_score, \
    log_loss, \
    matthews_corrcoef, \
    precision_score, \
    recall_score, \
    zero_one_loss


def classification_metrics(df):
    return {
        "accuracy_score": accuracy_score(df["y_pred"], df["y_test"]),
        "average_precision_score": average_precision_score(df["y_pred"], df["y_test"]),
        "f1_score": f1_score(df["y_pred"], df["y_test"]),
        "jaccard_score": jaccard_score(df["y_pred"], df["y_test"]),
        "log_loss": log_loss(df["y_pred"], df["y_test"]),
        "matthews_corrcoef": matthews_corrcoef(df["y_pred"], df["y_test"]),
        "precision_score": precision_score(df["y_pred"], df["y_test"]),
        "recall_score": recall_score(df["y_pred"], df["y_test"]),
        "zero_one_loss": zero_one_loss(df["y_pred"], df["y_test"])
    }


if __name__ == "__main__":
    with mlflow.start_run(run_name="evaluate_model") as run:
        mlflow.set_tag("mlflow.runName", "evaluate_model")
        df = pd.read_csv("data/predictions/test_predictions.csv")
        metrics = classification_metrics(df)
        mlflow.log_metrics(metrics)
