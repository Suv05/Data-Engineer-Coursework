FROM apache/airflow:3.0.0

USER root

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    default-libmysqlclient-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

USER airflow

# Install additional Python packages if needed
# RUN pip install --no-cache-dir package-name