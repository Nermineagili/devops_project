from flask import Flask, request, jsonify
import tensorflow as tf
import base64
import numpy as np
import librosa
import io

app = Flask(__name__)

# Load VGGish model
vggish_model = tf.keras.models.load_model('../models/vggish_model.pb')

@app.route('/predict_vgg', methods=['POST'])
def predict_vgg():
    # Get the base64 audio file from the request
    audio_data = request.json['wav_music']
    
    # Decode the base64 audio
    audio_bytes = base64.b64decode(audio_data)
    
    # Process audio
    waveform, sr = librosa.load(io.BytesIO(audio_bytes), sr=16000)
    
    # Prepare input for VGGish model
    inp = np.array([waveform]).astype('float32')
    
    # Make a prediction using the VGGish model
    class_scores = vggish_model.predict(inp)[0]
    genre = class_scores.argmax()

    return jsonify({'genre': genre})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002)
 