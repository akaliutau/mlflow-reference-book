import argparse
import sys

import mlflow
import click
import os


def _run(entrypoint, parameters: dict = None):
    if parameters is None:
        parameters = {}
    print("Launching new run for entrypoint=%s and parameters=%s" % (entrypoint, parameters))
    submitted_run = mlflow.run(".", entrypoint, parameters=parameters, env_manager='local')
    return mlflow.tracking.MlflowClient().get_run(submitted_run.run_id)


@click.command()
def workflow():
    with mlflow.start_run(run_name="pystock-training") as active_run:
        mlflow.set_tag("mlflow.runName", "full-cycle-training-plus-logging")
        train_run = _run("train_model")
        evaluate_run = _run("evaluate_model")
        model_uri = os.path.join(active_run.info.artifact_uri, "model")
        register_run = _run("register_model", {"model_uri": model_uri})


if __name__ == "__main__":
    workflow()
