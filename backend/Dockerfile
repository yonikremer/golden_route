FROM python:3.9-slim-buster

COPY /backend/ .
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "http_service:app", "--host", "0.0.0.0", "--port", "8000"]

