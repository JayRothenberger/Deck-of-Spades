FROM python:3.10-slim
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0
RUN apt-get update
RUN apt-get install -y gcc g++
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
WORKDIR /src
COPY . .
WORKDIR /src/piqueserver
RUN pip install -r requirements.txt
RUN pip install .
EXPOSE 32887/udp 32887 32886 32885
RUN piqueserver -c '/src/piqueserver/piqueserver/config/config.toml' -d '/src/piqueserver/piqueserver/config/'