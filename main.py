import os
from flask import Flask, request, send_file, jsonify, after_this_request
import edge_tts
import asyncio
from uuid import uuid4
from voices import voices
from flask_restx import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app, version='1.0', title='Text-to-Speech API', description='API do konwersji tekstu na mowę', doc='/')  # Dokumentacja dostępna na '/'


ns = api.namespace('tts', description='Operacje konwersji tekstu na mowę')


TEMP_DIR = "temp_audio"

if not os.path.exists(TEMP_DIR):
    os.makedirs(TEMP_DIR)


post_parser = reqparse.RequestParser()
post_parser.add_argument('text', type=str, required=True, help='Tekst do zamiany na dźwięk')
post_parser.add_argument('voice', type=str, default='pl-PL-ZofiaNeural', help='Nazwa głosu do użycia z listy dostępnych głosów')


async def generate_audio(text, voice, output_file):
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(output_file)


@ns.route('/convert-text-to-audio/')
class ConvertTextToAudio(Resource):
    @ns.doc(description="Zamienia tekst na plik audio w formacie MP3", responses={
        200: 'Sukces',
        400: 'Błędne żądanie',
        500: 'Błąd serwera'
    })
    @ns.expect(post_parser)
    def post(self):
        args = post_parser.parse_args()
        text = args['text']
        voice = args['voice']
        output_file = os.path.join(TEMP_DIR, f"{uuid4()}.mp3")

        available_voices = [v['Name'] for v in voices]
        if voice not in available_voices:
            return jsonify({'error': f'Voice {voice} is not available. Choose a valid voice from /available-voices.'}), 400

        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(generate_audio(text, voice, output_file))

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


@ns.route('/available-voices')
class AvailableVoices(Resource):
    @ns.doc(description="Zwraca listę dostępnych głosów")
    def get(self):
        return jsonify(voices)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
