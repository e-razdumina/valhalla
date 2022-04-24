FROM python:3.8
LABEL maintainer="e.razdumina@gmail.com"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN mongoimport -d flask_db -c valhalla db.json
EXPOSE 8180
EXPOSE 8181

COPY ./docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]
