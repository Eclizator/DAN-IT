
FROM python:3.9-slim


WORKDIR /app


COPY python-random.py /app/python-random.py


RUN pip install flask


EXPOSE 5000


CMD ["python", "python-random.py"]
