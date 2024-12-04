document.getElementById('svm-form').addEventListener('submit', async (event) => {
    event.preventDefault();
    const file = document.getElementById('svm-audio').files[0];
    const formData = new FormData();
    formData.append('file', file);

    try {
        const response = await fetch('http://localhost:8000/classify', {
            method: 'POST',
            body: formData
        });
        const result = await response.text();
        document.getElementById('svm-result').innerHTML = result;
    } catch (error) {
        document.getElementById('svm-result').innerHTML = 'Error: ' + error;
    }
});

document.getElementById('vgg-form').addEventListener('submit', async (event) => {
    event.preventDefault();
    const file = document.getElementById('vgg-audio').files[0];
    
    const reader = new FileReader();
    reader.onload = async () => {
        const base64Audio = reader.result.split(',')[1];
        try {
            const response = await fetch('http://localhost:5002/predict_vgg', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ wav_music: base64Audio })
            });
            const data = await response.json();
            document.getElementById('vgg-result').innerText = `Predicted Genre (VGG): ${data.genre}`;
        } catch (error) {
            document.getElementById('vgg-result').innerText = 'Error: ' + error;
        }
    };
    reader.readAsDataURL(file);
});
