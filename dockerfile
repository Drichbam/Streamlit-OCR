# 1. Select base image from which we build the container
FROM python:3.12-slim-bookworm

# 2. Set environment variables both at build and at run time.
# In this case, we make sure Python output is visible in Docker logs.
ENV PYTHONUNBUFFERED=1

# 3. Copy only requirements file to the container
COPY requirements.txt  /app/

# 4. Set working directoy from now on (like cd ... )
WORKDIR /app

# 5. Install python dependencies from requirements.txt
RUN python3 -m pip install --no-cache-dir -r requirements.txt

# 6. Copy the rest of application code to the container
COPY . /app

# streamlit specifics
EXPOSE 8501
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# 7. Set default command when container starts.
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
