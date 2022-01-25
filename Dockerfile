# sudo docker buildx build -t metrics_exporter . --platform linux/amd64
# sudo docker tag metrics_exporter zukunft/metrics_exporter:1.5.10

FROM python:3.8 AS builder
COPY requirements.txt .
RUN pip install --user -r requirements.txt
FROM python:3.8-slim
WORKDIR /
COPY --from=builder /root/.local /root/.local
COPY src/ /src
COPY config/ config/
EXPOSE 8080
ENV PATH=/root/.local:$PATH
CMD sh /src/start.sh