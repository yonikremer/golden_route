FROM python:3.9-slim-buster

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY http_service.py .

EXPOSE 8000

CMD ["uvicorn", "http_service:app", "--host", "0.0.0.0", "--port", "8000"]

