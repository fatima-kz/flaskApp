# syntax=docker/dockerfile:1.4
# Use official lightweight Python image
FROM python:3.10-slim

# Set working dir
WORKDIR /app

# Copy requirements first to leverage build cache
COPY requirements.txt .
# Use BuildKit cache for pip to speed up subsequent builds
ENV PIP_DISABLE_PIP_VERSION_CHECK=1 \
	PYTHONDONTWRITEBYTECODE=1 \
	PYTHONUNBUFFERED=1
RUN --mount=type=cache,target=/root/.cache/pip \
	pip install -r requirements.txt

# Copy app
COPY . .

# Expose port and run
EXPOSE 5000
ENV FLASK_APP=app.py
CMD ["python", "app.py"]
