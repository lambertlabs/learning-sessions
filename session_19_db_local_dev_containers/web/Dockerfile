FROM python:3.8.2-slim-buster

ARG PROJECT_DIR="demo5"
RUN mkdir $PROJECT_DIR
WORKDIR $PROJECT_DIR
COPY model model
COPY web .
RUN python -m pip install --upgrade pip
RUN pip install --requirement requirements.txt
EXPOSE 8000
CMD ["python", "app.py"]
