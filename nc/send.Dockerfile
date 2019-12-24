FROM python:3-slim
RUN apt update && apt install -y netcat
ARG file_change
ADD send.py .
ENTRYPOINT python -u send.py