# About 

A handbook + runbook for typical installations and experiments with MLFlow, Jupiter Notebooks, scikit-learn and other useful tools

# 00 Quickly run local instance of jupiter notebook (with classic Iris flowers classification problem)

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

# 01 End-to-end pipeline in MLflow: random forest linear regression for stock exchange prices

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



