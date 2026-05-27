FROM python:3.11-slim

WORKDIR /app

RUN adduser --disabled-password appuser

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chown -R appuser /app

USER appuser

EXPOSE 5000

CMD ["python", "src/app.py"]