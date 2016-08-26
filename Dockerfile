FROM daocloud.io/library/python:2.7.11
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt

EXPOSE 5050
CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:5050", "app:app"]
