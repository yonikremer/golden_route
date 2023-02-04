# Strat with a python 3.9 base image
FROM python:3.9

COPY /backend/ .
COPY /backend/ /backend
COPY /backend/requirements.txt .
RUN pip install --no-cache-dir -r backend/requirements.txt
ENV PYTHONPATH "${PYTHONPATH}:/backend"

EXPOSE 8000

CMD ["uvicorn", "http_service:app", "--host", "0.0.0.0", "--port", "8000"]

