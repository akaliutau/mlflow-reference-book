# About 

A handbook + runbook for typical installations and experiments with MLFlow, Jupiter Notebooks, scikit-learn and other useful tools

# 00 Quickly run local instance of jupiter notebook

(with classic Iris flowers classification problem)

```shell
sudo docker build -t jpnotebook .

mkdir -p "$HOME/notebooks"
export JUPYTER_TOKEN='123'

sudo docker run -p 8888:8888 -p 5000:5000 \
  -u "$(id -u ${USER})":"$(id -g ${USER})" \
  -e JUPYTER_TOKEN=$JUPYTER_TOKEN \
  -v "$HOME/notebooks/":/home/jovyan/ -it jpnotebook
```
Jupiter server entry point is available at localhost:8888

Use token set in JUPYTER_TOKEN for authentication and copy your .ipynb to "$HOME/notebooks" 

Use CTRL + SHIFT + C to stop Jupiter server

The `mlruns` folder will be generated in root notebook folder and will contain all experiments 
with a sequential number as an experiment id.  

The serialized model is put fe. into the following path:
`mlruns/0/c7f213c6530b4622a4d87a78264df7f4/artifacts/model/model.pkl`

# 01 Training job in MLflow: random forest linear regression for stock exchange prices (local env or docker)

(using original data from yahoo API: https://finance.yahoo.com/quote/BTC-USD/)

The core idea: choose 14-days vectors and try to predict the next price move (closes higher or lower)

For development install all deps locally in `01-*` folder:

```shell
python3 -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt
```

Check model is working in local runtime env:

```shell
 python3 -m 01-random-forest-price-predictor.train
```

Building model and running inference endpoint:

1) build image with mlflow toolkit:

```shell
sudo docker build -t dmlflow .
```

2) run mlflow (from `01-*` project directory)

```shell
sudo docker run -v $(pwd):/mlflow/ -p 5000:5000 -it dmlflow mlflow run /mlflow/ --env-manager=local
```

3) the local equivalent of the same command:

```shell
mlflow run . --env-manager=local
```

4) check the models stat:

```shell
mlflow ui
```

6) serve the selected best model:

```shell
mlflow models serve -m runs:/<my-run-id>/<model-path> &

fe.

mlflow models serve -m runs:/3b10ad2ebd0a4600bd660d0d109ea1e9/model_random_forest  --env-manager=local
```
Predictions can be made via invoking endpoint which is exposing the chosen model:

```shell
curl -X POST  localhost:5000/invocations -H 'Content-Type: application/json' -d '{"inputs":[[1,1,1,1,0,1,1,1,0,1,1,1,0,0]]}'
```

# 02 Running full training cycle at mlflow (docker)

1) build image with mlflow toolkit:

```shell
sudo docker build -t dmlflow .
```

2) run mlflow (from `02-*` project directory)

```shell
sudo docker run -v $(pwd)/training_project:/workdir/ -p 5000:5000 -it dmlflow --env-manager=local
```

After successful completion the directory `mlruns` will contain the result of run and experiment details