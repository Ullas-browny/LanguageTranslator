from flask import Flask, request, jsonify
from translate import Translator
import os

app = Flask(__name__)
translator = Translator(from_lang='en', to_lang='hi')

def translate_text(text):
    batch_size = 500
    batches = [text[i:i + batch_size] for i in range(0, len(text), batch_size)]
    translated_batches = [translator.translate(batch) for batch in batches]
    return ''.join(translated_batches)

@app.route('/translate', methods=['POST'])
def translate_route():
    data = request.get_json()
    print("Received data:", data)
    if 'text' not in data:
        return jsonify({'error': 'No text provided'}), 400

    text = data['text']
    translated_text = translate_text(text)
    print(translated_text)
    return jsonify({'translated_text': translated_text})

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))  # Default to 5000 if not set
    app.run(debug=True, port=port)
