from flask import Flask, request, jsonify
import tensorflow as tf
import base64
import numpy as np
import librosa
import io

app = Flask(__name__)

@app.route('/health')
def health_check():
    return "Service is healthy", 200

# Load VGGish model - TensorFlow models are usually saved in the SavedModel format for TensorFlow 2.x
vggish_model = tf.saved_model.load('vgg_19_service/vggish_model.pb')

@app.route('/predict_vgg', methods=['POST'])
def predict_vgg():
    try:
        # Get the base64 audio file from the request
        audio_data = request.json['wav_music']

        # Decode the base64 audio
        audio_bytes = base64.b64decode(audio_data)
        
        # Process audio
        waveform, sr = librosa.load(io.BytesIO(audio_bytes), sr=16000)

        # Ensure the waveform is of the correct shape (1, n_samples)
        waveform = waveform.reshape(1, -1)

        # Prepare input for VGGish model
        # It's possible that VGGish expects some specific preprocessing steps. 
        # Ensure that your preprocessing is correctly handled if needed.
        inp = np.array([waveform]).astype('float32')
        
        # Make a prediction using the VGGish model
        # Note: Adjust model prediction as per your actual model output
        infer = vggish_model.signatures['serving_default']
        class_scores = infer(tf.convert_to_tensor(inp))[0].numpy()

        # Get the genre with the highest score
        genre = np.argmax(class_scores)

        return jsonify({'genre': genre})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002)
