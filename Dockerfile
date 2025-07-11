FROM python:3.9-slim

WORKDIR /app

COPY . /app

# ✅ Install required build tools for packages like `blis`
RUN apt-get update && apt-get install -y gcc g++ python3-dev build-essential

# ✅ Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# ✅ Download spaCy model
RUN python -m spacy download en_core_web_sm

EXPOSE 5000

CMD ["python", "app.py"]
