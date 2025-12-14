FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libx11-6 \
    libxext6 \
    libxrender1 \
    libxrandr2 \
    libxi6 \
    libxfixes3 \
    libxcursor1 \
    libxdamage1 \
    libxcomposite1 \
    libglib2.0-0 \
    libasound2 \
    libpulse0 \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy agent code
COPY agent.py .

# Run the agent
CMD ["python", "agent.py", "start"]
