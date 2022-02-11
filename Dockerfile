FROM python:3.10-slim

ADD app.py requirements.txt ./

RUN apt-get update && apt-get install --no-install-recommends -y gcc libc6-dev && pip install -r requirements.txt

ENTRYPOINT ["python", "app.py"]
