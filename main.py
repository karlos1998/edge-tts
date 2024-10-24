import os
from flask import Flask, request, send_file, jsonify, after_this_request
import edge_tts
import asyncio
from uuid import uuid4
from voices import voices

app = Flask(__name__)

TEMP_DIR = "temp_audio"


# Tworzenie katalogu na pliki tymczasowe
if not os.path.exists(TEMP_DIR):
    os.makedirs(TEMP_DIR)


async def generate_audio(text, voice, output_file):
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(output_file)


@app.route('/convert-text-to-audio/', methods=['POST'])
def convert_text_to_audio():
    try:
        text = request.form.get('text')
        voice = request.form.get('voice', 'pl-PL-ZofiaNeural')  # domyślny głos, jeśli nie podano
        output_file = os.path.join(TEMP_DIR, f"{uuid4()}.mp3")

        # Sprawdzenie, czy podany głos istnieje w liście dostępnych głosów
        available_voices = [v['Name'] for v in voices]
        if voice not in available_voices:
            return jsonify({'error': f'Voice {voice} is not available. Choose a valid voice from /available-voices.'}), 400

        # Użycie asyncio.run() wewnątrz funkcji synchronizowanej Flask
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(generate_audio(text, voice, output_file))

        # Sprawdzanie, czy plik został poprawnie wygenerowany
        if not os.path.exists(output_file) or os.path.getsize(output_file) == 0:
            return jsonify({'error': 'Audio file generation failed.'}), 500

        @after_this_request
        def remove_file(response):
            try:
                os.remove(output_file)
            except Exception as error:
                print(f"Error removing or cleaning up file: {error}")
            return response

        return send_file(output_file, as_attachment=True, download_name='output.mp3', mimetype='audio/mpeg')

    except KeyError:
        return jsonify({'error': 'Missing "text" parameter in request.'}), 400

    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Endpoint do uzyskania listy dostępnych głosów
@app.route('/available-voices', methods=['GET'])
def get_available_voices():
    return jsonify(voices)


# Uruchamianie serwera
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
