FROM python:3.10-slim

WORKDIR /app

COPY services/model-service/app /app
COPY model/artifacts /app/model/artifacts
COPY requirements.txt /app

RUN pip install --no-cache-dir -r requirements.txt

ENV PORT=8080
EXPOSE 8080

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
