# Lightweight Python image
FROM python:3.10-slim

# Avoid interactive prompts & speed up pip
ENV DEBIAN_FRONTEND=noninteractive \
    PIP_NO_CACHE_DIR=1 \
    PYTHONUNBUFFERED=1

# Workdir
WORKDIR /app

# System deps (optional but good for scientific wheels)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential curl && \
    rm -rf /var/lib/apt/lists/*

# Copy requirements first (better caching)
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest (quotes handle space in folder name)
COPY . /app

# Expose port expected by Spaces
EXPOSE 7860

# Streamlit needs to bind to 0.0.0.0 and pick up $PORT (Spaces sets it)
CMD streamlit run app.py --server.address 0.0.0.0 --server.port $PORT
