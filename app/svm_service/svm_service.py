# from flask import Flask, request, jsonify
# import joblib
# import librosa
# import numpy as np
# import os
# import sklearn

# # Base path for loading and saving files
# BASE_PATH = os.path.dirname(os.path.abspath(__file__))

# # Load the pre-trained SVM model
# MODEL_PATH = os.path.join(BASE_PATH, 'svm_model.pkl')
# svm_model = joblib.load(MODEL_PATH)

# # Flask application
# app = Flask(__name__)

# # Feature extraction functions
# def normalize(x, axis=0):
#     return sklearn.preprocessing.minmax_scale(x, axis=axis)

# def zero_cross(x):
#     n0 = 9000
#     n1 = 9100
#     zero_crossings = librosa.zero_crossings(x[n0:n1], pad=False)
#     return sum(zero_crossings)

# def spec_center(x, sr):
#     spectral_centroids = normalize(librosa.feature.spectral_centroid(y=x, sr=sr)[0])
#     frames = range(len(spectral_centroids))
#     t = librosa.frames_to_time(frames)
#     ma = max(spectral_centroids)
#     return t[np.where(spectral_centroids == ma)[0][0]]

# def extract_features(filename):
#     x, sr = librosa.load(filename)
#     features = [zero_cross(x), round(spec_center(x, sr), 2)]
#     return np.array(features).reshape(1, -1)

# @app.route('/classify', methods=['POST'])
# def classify_genre():
#     if 'file' not in request.files:
#         return jsonify({"error": "No file provided"}), 400

#     file = request.files['file']
#     try:
#         TEMP_AUDIO_PATH = os.path.join(BASE_PATH, 'temp_audio.wav')
#         file.save(TEMP_AUDIO_PATH)
#         features = extract_features(TEMP_AUDIO_PATH)
#         prediction = svm_model.predict(features)

#         genre_map = {'hiphop': "Hip-Hop", 'pop': "Pop", 'blues': "Blues", 'metal': "Metal"}
#         genre = genre_map.get(prediction[0], "Unknown Genre")

#         return jsonify({"genre": genre}), 200
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# if __name__ == '__main__':
#     app.run(debug=True, port=8000)






























































# from flask import Flask, request, jsonify
# import joblib
# import librosa
# import numpy as np
# import os
# import sklearn
# import requests  # For communication with VGGish service

# # Base path for loading and saving files
# BASE_PATH = os.path.dirname(os.path.abspath(__file__))

# # Load the pre-trained SVM model
# MODEL_PATH = os.path.join(BASE_PATH, 'svm_model.pkl')  # Adjust if needed
# svm_model = joblib.load(MODEL_PATH)

# # Flask application
# app = Flask(__name__)

# # Feature extraction functions
# def normalize(x, axis=0):
#     return sklearn.preprocessing.minmax_scale(x, axis=axis)

# def zero_cross(x):
#     n0 = 9000
#     n1 = 9100
#     zero_crossings = librosa.zero_crossings(x[n0:n1], pad=False)
#     return sum(zero_crossings)

# def spec_center(x, sr):
#     spectral_centroids = normalize(librosa.feature.spectral_centroid(y=x, sr=sr)[0])
#     frames = range(len(spectral_centroids))
#     t = librosa.frames_to_time(frames)
#     ma = max(spectral_centroids)
#     return t[np.where(spectral_centroids == ma)[0][0]]

# # Function to extract features from an audio file
# def extract_features(filename):
#     x, sr = librosa.load(filename)
#     features = [zero_cross(x), round(spec_center(x, sr), 2)]
#     return np.array(features).reshape(1, -1)

# @app.route('/classify', methods=['POST'])
# def classify_genre():
#     if 'file' not in request.files:
#         return jsonify({"error": "No file provided"}), 400

#     file = request.files['file']

#     try:
#         TEMP_AUDIO_PATH = os.path.join(BASE_PATH, 'temp_audio.wav')
#         file.save(TEMP_AUDIO_PATH)

#         # Optional: Send file to VGGish service
#         with open(TEMP_AUDIO_PATH, 'rb') as audio_file:
#             vggish_response = requests.post("http://vggish_service:5002/process", files={"file": audio_file})

#         if vggish_response.status_code == 200:
#             vggish_data = vggish_response.json()
#             print("VGGish response:", vggish_data)

#         features = extract_features(TEMP_AUDIO_PATH)
#         prediction = svm_model.predict(features)

#         genre_map = {'hiphop': "Hip-Hop", 'pop': "Pop", 'blues': "Blues", 'metal': "Metal"}  # Adjust as needed
#         genre = genre_map.get(prediction[0], "Unknown Genre")

#         return jsonify({"genre": genre, "vggish_data": vggish_data})

#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# if __name__ == '__main__':
#     app.run(debug=True, port=8000)

















































































from flask import Flask, request, jsonify, render_template_string
import joblib
import librosa
import numpy as np
import os
import sklearn

# Base path for loading and saving files
BASE_PATH = os.path.dirname(os.path.abspath(__file__))

# Load the pre-trained SVM model
MODEL_PATH = os.path.join(BASE_PATH, 'svm_model.pkl')  # Assuming your model is named 'svm_model.pkl'
svm_model = joblib.load(MODEL_PATH)

# Flask application
app = Flask(__name__)

# HTML Template for Upload Form
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Audio Genre Classification</title>
</head>
<body>
    <h1>Upload an Audio File</h1>
    <form action="/classify" method="post" enctype="multipart/form-data">
        <input type="file" name="file" accept="audio/*" required>
        <button type="submit">Classify</button>
    </form>
</body>
</html>
"""

# Feature extraction functions (from the provided model code)
def normalize(x, axis=0):
    return sklearn.preprocessing.minmax_scale(x, axis=axis)

def zero_cross(x):
    n0 = 9000
    n1 = 9100
    zero_crossings = librosa.zero_crossings(x[n0:n1], pad=False)
    return sum(zero_crossings)

def spec_center(x, sr):
    # Extract the spectral centroid using keyword arguments
    spectral_centroids = normalize(librosa.feature.spectral_centroid(y=x, sr=sr)[0])
    
    # Get the time frames corresponding to the spectral centroids
    frames = range(len(spectral_centroids))
    t = librosa.frames_to_time(frames)
    
    # Find the maximum spectral centroid and return the corresponding time
    ma = max(spectral_centroids)
    return t[np.where(spectral_centroids == ma)[0][0]]

# Function to extract features from an audio file
def extract_features(filename):
    # Load the audio file
    x, sr = librosa.load(filename)
    
    # Extract features: zero crossing rate and spectral centroid
    features = [zero_cross(x), round(spec_center(x, sr), 2)]
    
    return np.array(features).reshape(1, -1)

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/classify', methods=['POST'])
def classify_genre():
    if 'file' not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files['file']

    try:
        # Save the file temporarily
        TEMP_AUDIO_PATH = os.path.join(BASE_PATH, 'temp_audio.wav')
        file.save(TEMP_AUDIO_PATH)

        # Extract features from the audio file
        features = extract_features(TEMP_AUDIO_PATH)

        # Predict the genre using the pre-trained model
        prediction = svm_model.predict(features)

        # Map prediction to human-readable label (adjust genre map as needed)
        genre_map = {'hiphop': "Hip-Hop", 'pop': "Pop", 'blues': "Blues", 'metal': "Metal"}  # Update as needed
        genre = genre_map.get(prediction[0], "Unknown Genre")

        return f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Genre Prediction</title>
        </head>
        <body>
            <h1>Prediction Result</h1>
            <p>The predicted genre is: <strong>{genre}</strong></p>
            <a href="/">Classify another file</a>
        </body>
        </html>
        """

    except Exception as e:
        return f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Error</title>
        </head>
        <body>
            <h1>An error occurred</h1>
            <p>{str(e)}</p>
            <a href="/">Try again</a>
        </body>
        </html>
        """

if __name__ == '__main__':
    app.run(debug=True, port=8000)
