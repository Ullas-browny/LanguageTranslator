from flask import Flask, request, jsonify
app = Flask(__name__)
from translate import Translator

@app.route('/')
def hello_world():
    return 'Hello, World!'

translator = Translator(from_lang='en', to_lang='hi')

def translate_text(text):
    # Split text into 500-character batches
    batch_size = 500
    batches = [text[i:i + batch_size] for i in range(0, len(text), batch_size)]
    
    # Translate each batch and join the results
    translated_batches = [translator.translate(batch) for batch in batches]
    return ''.join(translated_batches)

@app.route('/translate', methods=['POST'])
def translate_route():
    data = request.get_json()
    print("Received data:", data)  # Add this line
    if 'text' not in data:
        return jsonify({'error': 'No text provided'}), 400

    text = data['text']  # This should print the text
    translated_text = translate_text(text)
    print(translated_text)
    return jsonify({'translated_text': translated_text})
