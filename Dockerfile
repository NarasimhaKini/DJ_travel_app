FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y build-essential libpq-dev

COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir --root-user-action=ignore -r requirements.txt
COPY . .

# collectstatic during build (optional — env must have correct vars)
# RUN python manage.py collectstatic --noinput

CMD ["gunicorn", "dj_travel_app.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]
