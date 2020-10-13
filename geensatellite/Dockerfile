FROM continuumio/miniconda3
ENV PYTHONUNBUFFERED=1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN conda install --file=requirements.txt
COPY . /code/