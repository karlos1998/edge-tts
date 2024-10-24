# Używamy obrazu bazowego Python 3.9
FROM python:3.9-slim

# Ustawienie katalogu roboczego
WORKDIR /app

# Skopiowanie pliku requirements.txt do kontenera
COPY requirements.txt requirements.txt

# Instalacja zależności
RUN pip install --no-cache-dir -r requirements.txt

# Skopiowanie wszystkich plików aplikacji do kontenera
COPY . .

# Uruchomienie aplikacji Flask
CMD ["flask", "run", "--host=0.0.0.0", "--port=5001"]
