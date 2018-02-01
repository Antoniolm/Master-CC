FROM frolvlad/alpine-python3

MAINTAINER Antonio David López Machado <antdlopma@gmail.com>
WORKDIR /app

ADD static/style.css /app/static/style.css
ADD templates/index.html /app/templates/index.html

RUN apk update && apk upgrade
RUN apk add git

RUN pip3 install flask pytest pymongo
COPY ./service.py /app

ENTRYPOINT ["python"]
CMD ["service.py"]
