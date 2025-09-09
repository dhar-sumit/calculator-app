FROM python:3.10-slim

WORKDIR /app

COPY calc.py test_calc.py ./

RUN python -m unittest test_calc.py

CMD ["python", "-m", "unittest", "test_calc.py"]
