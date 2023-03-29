FROM python:3.11-slim
WORKDIR /app
COPY ./requirements.txt .
RUN pip3 install -r requirements.txt --no-cache-dir
COPY hire_hire/ .
CMD ["gunicorn", "hire_hire.wsgi:application", "--bind", "0:8000" ]