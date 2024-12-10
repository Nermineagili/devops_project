import pytest
import io
from flask.testing import FlaskClient
from werkzeug.datastructures import FileStorage
from svm_service import app


@pytest.fixture
def client():
    """Fixture to provide a test client for the Flask app."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_route(client: FlaskClient):
    """Test the index route to ensure the service is running."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'"message":"SVM Service is running"' in response.data

def test_classify_no_file(client: FlaskClient):
    """Test the classify route when no file is provided."""
    response = client.post('/classify')
    assert response.status_code == 400
    assert b"No file provided" in response.data

# def test_classify_with_valid_file(client: FlaskClient):
#     """Test the classify route with a valid audio file."""
#     dummy_audio_data = io.BytesIO(b"Dummy audio data")
#     dummy_audio_file = FileStorage(
#         stream=dummy_audio_data,
#         filename="test_audio.wav",
#         content_type="audio/wav"
#     )

#     response = client.post(
#         '/classify',
#         content_type='multipart/form-data',
#         data={'file': dummy_audio_file}
#     )

#     assert response.status_code == 200
#     assert b"The predicted genre is" in response.data or b"An error occurred" in response.data

# def test_classify_with_invalid_file(client: FlaskClient):
#     """Test the classify route with an invalid file (non-audio)."""
#     invalid_file_data = io.BytesIO(b"Not an audio file")
#     invalid_file = FileStorage(
#         stream=invalid_file_data,
#         filename="test_invalid.txt",
#         content_type="text/plain"
#     )

#     response = client.post(
#         '/classify',
#         content_type='multipart/form-data',
#         data={'file': invalid_file}
#     )

#     assert response.status_code == 400
#     assert b"Invalid file type" in response.data
