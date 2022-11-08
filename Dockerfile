FROM python:3.9-alpine

ENV VIRTUAL_ENV=/opt/venv
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install dependencies:
RUN pip install --index-url="http://pypi-registry:4000" --trusted-host="pypi-registry" --no-cache-dir monitoring
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN mkdir -p /app/files

# Run the application:
COPY . .
CMD ["python", "main.py"]
