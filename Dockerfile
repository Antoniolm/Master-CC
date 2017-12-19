FROM frolvlad/alpine-python3

MAINTAINER Antonio David López Machado <antdlopma@gmail.com>
WORKDIR /app

RUN apk update && apk upgrade
RUN apk add git

RUN pip3 install flask pytest boto3
COPY contenedores/service.py /app

ENTRYPOINT ["python"]
CMD ["service.py"]
