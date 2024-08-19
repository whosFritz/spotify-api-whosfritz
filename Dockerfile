ARG PYTHON_VERSION=3.9.6
FROM python:${PYTHON_VERSION}-slim as base

# Prevent Python from writing pyc files.
ENV PYTHONDONTWRITEBYTECODE=1
# Keeps Python from buffering stdout and stderr.
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Set the timezone
ENV TZ=Europe/Berlin
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Install dependencies
COPY requirements.txt .
RUN python -m pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Run the application
CMD ["python", "getFavSong.py"]
