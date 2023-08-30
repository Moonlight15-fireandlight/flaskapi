FROM python:3.9-alpine

#RUN apk update
#
#RUN apk add py-pip
#
#RUN apk add --no-cache python3-dev 

RUN pip install --upgrade pip

WORKDIR /app

COPY . /app

RUN pip --no-cache-dir install -r requirements.txt

CMD ["python3", "app.py"]

#ENV AWS_ACCESS_KEY_ID="AKIA6GAKQC4RYEFPT6X2"
#
#ENV AWS_SECRET_ACCESS_KEY="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"
#
#ENV AWS_DEFAULT_REGION="us-east-1"
#
#ENV NAME_TABLE = "flaskapidemo"

