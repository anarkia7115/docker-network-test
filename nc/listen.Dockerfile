FROM python:3-slim
RUN apt update && apt install -y netcat
ARG file_change
ADD listen.py .
ENTRYPOINT python listen.py