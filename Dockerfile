FROM circleci/python:3.8

WORKDIR /app

COPY requirements.txt /app
<<<<<<< HEAD

=======
>>>>>>> 8baa30677683ec18066b8ada212484f4580885fb
RUN pip3 install -r requirements.txt

COPY . /app

ENTRYPOINT ["python3"]
CMD ["flask_app.py"]