FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8
COPY ./api /api
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
WORKDIR /api
