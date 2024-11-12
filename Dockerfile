FROM python:3.11

WORKDIR /code

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

COPY  ./requirements.txt /code/requirements.txt

COPY  src/fourthproject/main.py /code/
COPY  src/fourthproject/autoscale.py /code/
COPY  src/fourthproject/docker-compose.yml /code/

COPY  src/fourthproject/pages/ /code/pages/

RUN pip install -r requirements.txt

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
