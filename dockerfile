# Verwende ein offizielles Python-Laufzeit-Image als Basis
FROM python:3.9-slim

# Setze das Arbeitsverzeichnis im Container
WORKDIR /app

# Kopiere die requirements.txt in das Arbeitsverzeichnis
COPY requirements.txt .

# Installiere die Python-Abhängigkeiten
RUN pip install --no-cache-dir -r requirements.txt

# Kopiere den restlichen Code in das Arbeitsverzeichnis
COPY . .

# Setze die Umgebungsvariable für die MongoDB-URI
ENV MONGODB_URI="mongodb+srv://admin:123@cluster0.uvofxqx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Führe das Skript aus
CMD ["python", "Data.ipynb"]
