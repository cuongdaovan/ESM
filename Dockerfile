FROM python:3.6

WORKDIR /education

COPY . /education
COPY Pipfile Pipfile.lock ./

RUN pip install -U pipenv
RUN pipenv install --system

EXPOSE 8080

CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]
