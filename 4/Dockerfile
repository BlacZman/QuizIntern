FROM python:3-alpine
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE 1
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/
CMD [ "gunicorn", "4th-2:app", "--workers=4", "--bind", "0.0.0.0:8000" ]
