FROM python:alpine

WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt

COPY . .


EXPOSE 5000

CMD ["python", "-u", "app.py"]
