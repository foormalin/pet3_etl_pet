FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY etl/ ./etl/
COPY data/ ./data/
COPY sql/ ./sql/
CMD ["python", "etl/load.py"]
