FROM python:3.12-alpine

WORKDIR /app

COPY main.py .

ENTRYPOINT ["python", "main.py"]
CMD ["5"]
