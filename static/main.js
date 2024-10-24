document.getElementById('audio-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const formData = new FormData();
    formData.append('audio', document.getElementById('audio').files[0]);

    fetch('/process_audio', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            document.getElementById('result').textContent = data.error;
        } else {
            document.getElementById('result').innerHTML = `
                <p>Recognized Text: ${data.text}</p>
                <p>Health Advice: ${data.advice}</p>`;
        }
    })
    .catch(error => console.error('Error:', error));
});
