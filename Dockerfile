FROM python:3.8.10-slim

ENV DOCKERHOMEDIR /home/app
ENV PYTHONBUFFERED 1

RUN mkdir -p ${DOCKERHOMEDIR}

RUN apt-get update && apt-get install -y --no-install-recommends gcc && \
    apt-get install -y python3-dev && apt-get install -y default-libmysqlclient-dev && \
    pip install mysqlclient==2.0.1 && apt-get install -y build-essential && pip install --upgrade pip && \
    apt-get remove -y gcc && apt-get remove -y default-libmysqlclient-dev && apt-get remove -y build-essential

COPY . ${DOCKERHOMEDIR}

WORKDIR ${DOCKERHOMEDIR}

RUN pip install -r requirements.txt

# EXPOSE 9000

# CMD [ "python", "manage.py", "runserver" ]