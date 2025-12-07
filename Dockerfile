# 1. Base Image: Start with a lightweight Linux that has Python 3.11 installed
# "slim" means it's a smaller file size (good for DevOps!)
FROM python:3.11-slim

# 2. Work Directory: Create a folder inside the container called /app
# All future commands will run inside this folder
WORKDIR /app

# 3. Copy Requirements: Move the grocery list from your laptop to the container
COPY requirements.txt .

# 4. Install Dependencies: The container reads the list and installs libraries
# --no-cache-dir keeps the image small
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy Code: Move your python code (main.py) into the container
COPY . .

# 6. Expose Port: Tell Docker this container listens on port 8000
EXPOSE 8000

# 7. Start Command: The command to run when the container starts
# --host 0.0.0.0 is CRITICAL. It lets the container accept connections from outside.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]