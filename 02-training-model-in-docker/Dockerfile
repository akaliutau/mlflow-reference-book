FROM continuumio/miniconda3:23.10.0-1

RUN apt-get update && apt-get install build-essential -y

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

WORKDIR /workdir

ENTRYPOINT ["mlflow", "run", "."]


