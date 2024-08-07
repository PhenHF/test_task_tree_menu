FROM python:3.10.12-slim as builder

RUN mkdir app

WORKDIR app

ADD requirements.txt /app/
RUN pip install -r requirements.txt


ADD tree_menu_django_test_case .

RUN python3 manage.py makemigrations
RUN python3 manage.py migrate
RUN python3 manage.py create_test_user

CMD python3 manage.py runserver 0.0.0.0:8000