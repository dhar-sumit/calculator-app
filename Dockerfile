# Python 3.13 slim image
FROM python:3.13-slim

# Workdir inside the container
WORKDIR /app

# Copy only what we need
COPY calc.py test_calc.py ./

# Upgrade pip (no external deps needed for unittest)
RUN pip install --upgrade pip

# Default run: execute the unit tests
CMD ["python", "-m", "unittest", "-v", "test_calc.py"]
