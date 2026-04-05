FROM python:3.10-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files
COPY . .

# Expose ports for FastAPI (8000) and Streamlit (8501)
EXPOSE 8000 8501

# Copy a startup script
RUN chmod +x deployment/start.sh

# Run the startup script to boot both services
CMD ["bash", "deployment/start.sh"]
