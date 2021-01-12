FROM python:3.8.7-slim

RUN mkdir /app
WORKDIR /app
ADD ./app /app/
RUN pip install -r requirements.txt

EXPOSE 5000
CMD ["uvicorn", "app.api:app", "port", "5000"]