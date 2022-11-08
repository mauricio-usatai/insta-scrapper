FROM python:3.9-alpine

ENV VIRTUAL_ENV=/opt/venv
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install dependencies:
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN mkdir -p /app/files

# Run the application:
COPY . .
RUN pip install --index-url="http://host.docker.internal:4000" --trusted-host=host.docker.internal --no-cache-dir monitoring

CMD ["python", "main.py"]
