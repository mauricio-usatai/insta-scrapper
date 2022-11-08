FROM python:3.9-alpine

ENV VIRTUAL_ENV=/opt/venv
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install dependencies:
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN pip install --extra-index-url="http://192.168.0.174:4000" monitoring
RUN mkdir -p /app/files

# Run the application:
COPY . .
CMD ["python", "main.py"]