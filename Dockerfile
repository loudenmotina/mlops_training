FROM circleci/python:3.8

WORKDIR /app

COPY requirements.txt /app
RUN pip3 install -r requiements.txt

COPY . /app

ENTRYPOINT ["python3"]
CMD ["flask_app.py"]