FROM python:3.11

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

RUN mkdir ./feeding_calc
COPY . ./feeding_calc

RUN pip install gunicorn

EXPOSE 8000

CMD ["gunicorn", "--bind", ":8000", "feeding_calc.wsgi:app"]