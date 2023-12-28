import sys

import mlflow

if __name__ == "__main__":
    model_url = sys.argv[2]
    with mlflow.start_run(run_name="register_model") as run:
        mlflow.set_tag("mlflow.runName", "register_model")

        result = mlflow.register_model(
            model_url,
            "training-model-stock")
