FROM python:3.13-slim

WORKDIR /app

# Copy Python module and tests
COPY calc_app/ ./calc_app/
COPY tests/ ./tests/
COPY setup.py ./setup.py

RUN pip install --upgrade pip setuptools wheel

# Default run: execute tests
CMD ["python", "-m", "unittest", "discover", "-s", "tests"]



# # Python 3.13 slim image
# FROM python:3.13-slim

# # Workdir inside the container
# WORKDIR /app

# # Copy setup and module folder
# COPY setup.py .
# COPY calc_app/ ./calc_app

# # Install the package
# RUN pip install --no-cache-dir .

# # Copy tests
# COPY tests/ ./tests

# # Upgrade pip (optional, already inside slim image)
# RUN pip install --upgrade pip

# # Default run: execute the unit tests
# CMD ["python", "-m", "unittest", "discover", "-s", "tests"]
