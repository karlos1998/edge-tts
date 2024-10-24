
# Edge TTS Application

🇬🇧 **[English Version](#english-version)**  
🇵🇱 **[Polska Wersja](#polska-wersja)**

---

## English Version

This is a Flask-based Edge TTS application that allows converting text to speech using the Edge TTS service. The app provides two endpoints:
1. `/tts/convert-text-to-audio/` - Converts text into an audio file (MP3).
2. `/tts/available-voices` - Returns a list of available voices.

### Requirements

#### With Docker:
- Docker (https://docs.docker.com/get-docker/)
- Docker Compose (https://docs.docker.com/compose/install/)

#### Without Docker:
- Python 3.9 or newer (https://www.python.org/downloads/)
- Virtualenv (optional, but recommended)

### Installation

#### Using Docker:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-repo.git
   cd your-repo
   ```

2. **Run the application using Docker Compose:**
   ```bash
   docker-compose up --build
   ```

3. The application will be available at `http://localhost:5001`.

#### Without Docker:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-repo.git
   cd your-repo
   ```

2. **Create and activate a virtual environment (optional):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # For macOS/Linux
   # or
   venv\Scriptsctivate  # For Windows
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   export FLASK_APP=app.py
   flask run --host=0.0.0.0 --port=5001
   ```

   The application will be available at `http://localhost:5001`.

### Usage

#### 1. Convert Text to Speech:

The `POST /tts/convert-text-to-audio/` endpoint converts text into an MP3 file. For example:

```bash
curl -X POST http://localhost:5001/tts/convert-text-to-audio/ -F "text=This is a test" -o output.mp3
```

Once the request is processed, the `output.mp3` file will be downloaded.

#### 2. Get Available Voices:

The `GET /tts/available-voices/` endpoint returns a list of available voices:

```bash
curl http://localhost:5001/tts/available-voices
```

#### 3. Stop the application (Docker):

To stop the application when using Docker:

```bash
docker-compose down
```

### Testing

If you want to test the application using GitHub Actions, a test workflow is already set up in `.github/workflows`. To run the tests:

1. Tests will automatically run after each `push` to the repository.
2. You can also manually trigger the workflow in the `Actions` section of your GitHub repository.

### Additional Information

- In production environments, it is recommended to use WSGI (e.g., with `gunicorn`) to serve the Flask app.
- If you want to customize the app for your environment, you can modify environment variables in the `docker-compose.yml` file.

---

## Polska Wersja

To jest aplikacja Edge TTS oparta na Flask, która umożliwia konwersję tekstu na mowę za pomocą usługi Edge TTS. Aplikacja udostępnia dwa endpointy:
1. `/tts/convert-text-to-audio/` - konwertuje tekst na plik audio (MP3).
2. `/tts/available-voices` - zwraca listę dostępnych głosów.

### Wymagania

#### Z Dockerem:
- Docker (https://docs.docker.com/get-docker/)
- Docker Compose (https://docs.docker.com/compose/install/)

#### Bez Dockera:
- Python 3.9 lub nowszy (https://www.python.org/downloads/)
- Virtualenv (opcjonalnie, ale zalecane)

### Instalacja

#### Z użyciem Dockera:

1. **Klonowanie repozytorium:**
   ```bash
   git clone https://github.com/twoje-repo.git
   cd twoje-repo
   ```

2. **Uruchomienie aplikacji przy pomocy Docker Compose:**
   ```bash
   docker-compose up --build
   ```

3. Aplikacja będzie dostępna pod adresem `http://localhost:5001`.

#### Bez użycia Dockera:

1. **Klonowanie repozytorium:**
   ```bash
   git clone https://github.com/twoje-repo.git
   cd twoje-repo
   ```

2. **Tworzenie i aktywowanie środowiska wirtualnego (opcjonalnie):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Dla systemu macOS/Linux
   # lub
   venv\Scriptsctivate  # Dla Windows
   ```

3. **Instalacja zależności:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Uruchomienie aplikacji:**
   ```bash
   export FLASK_APP=app.py
   flask run --host=0.0.0.0 --port=5001
   ```

   Aplikacja będzie dostępna pod adresem `http://localhost:5001`.

### Użycie

#### 1. Konwersja tekstu na mowę:

Endpoint `POST /tts/convert-text-to-audio/` konwertuje tekst na plik MP3. W przykładzie poniżej wysyłamy tekst do konwersji:

```bash
curl -X POST http://localhost:5001/tts/convert-text-to-audio/ -F "text=To jest test" -o output.mp3
```

Po poprawnym działaniu aplikacji plik `output.mp3` zostanie pobrany.

#### 2. Pobranie listy dostępnych głosów:

Endpoint `GET /tts/available-voices/` zwraca listę dostępnych głosów:

```bash
curl http://localhost:5001/tts/available-voices
```

#### 3. Zatrzymanie aplikacji (Docker):

Aby zatrzymać aplikację uruchomioną przy użyciu Dockera:

```bash
docker-compose down
```

### Testowanie

Jeśli chcesz przetestować aplikację przy użyciu GitHub Actions, workflow do testów jest już skonfigurowany w `.github/workflows`. Aby uruchomić testy:

1. Po każdym `push` do repozytorium GitHub Actions automatycznie uruchomi testy.
2. Możesz również ręcznie uruchomić workflow w sekcji `Actions` swojego repozytorium na GitHubie.

### Dodatkowe informacje

- W środowisku produkcyjnym zaleca się używanie WSGI (np. z `gunicorn`) do uruchamiania aplikacji Flask.
- Jeśli chcesz dostosować aplikację do swojego środowiska, możesz zmienić zmienne środowiskowe w pliku `docker-compose.yml`.

