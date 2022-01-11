# docker buildx build -t metrics_exporter . --platform linux/amd64
# docker tag metrics_exporter zukunft/metrics_exporter:1.1.2

FROM python:3.8 AS builder
COPY requirements.txt .
RUN pip install --user -r requirements.txt
FROM python:3.8-slim
WORKDIR /code
COPY --from=builder /root/.local /root/.local
COPY ./src .
COPY ./config .
EXPOSE 8080
ENV PATH=/root/.local:$PATH
CMD ["python", "-u", "./main.py"]