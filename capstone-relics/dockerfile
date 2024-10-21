FROM python:3.10.12-slim-bookworm

WORKDIR ~/solar-simulator-hub/src/

COPY src/hub/ .

RUN pip3 install -r requirements.txt

#CMD ["ls"]
CMD ["python3", "solar-sim-hub.py", "4"]