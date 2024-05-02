# Use the official Python base image
FROM python:3.10

# cv2 deps
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6 poppler-utils tesseract-ocr -y

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install pytesseract

# Copy the rest of the application code to the container
COPY . .

# cmd shoud be bash: scripts/run.sh
# CMD ["bash", "/app/scripts/run.sh"]
# cmd shoud be python: scripts/run.py
CMD ["python3", "/app/scripts/run.py"]