# Face Emotion Analyzer

This repository contains the Face Emotion Analyzer, a Flask-based application that uses deep learning models to analyze emotions in images.

## Installation

Before running the application, you need to install the necessary packages. This can be done via pip:

```bash
pip install Flask deepface opencv-python
```
## Running the Flask Server
To start the Flask server, run the following command in your terminal:
```bash
python app.py
```

This will start the server on http://127.0.0.1:5000/.

## Using the Face Emotion Analyzer
### Sending an Image for Analysis
To analyze an image for emotions, you need to send a POST request to the Flask server. This can be done using PowerShell as follows:

```bash
Invoke-WebRequest -Uri http://127.0.0.1:5000/analyze -Method POST -Form @{file = Get-Item "C:\path\to\your\image.jpg"}
```
Replace "C:\path\to\your\image.jpg" with the path to the image you want to analyze.

## Receiving and Handling the Response
The Flask server responds with emotion analysis results in JSON format. You can handle this response in PowerShell:

```bash
$response = Invoke-WebRequest -Uri http://127.0.0.1:5000/analyze -Method POST -Form @{file = Get-Item "C:\path\to\your\image.jpg"}
$response.Content
```

This will display the JSON data returned by the Flask API.

If you want to handle this JSON data as a PowerShell object (for easier access to specific properties), you can convert it using ConvertFrom-Json:

```bash
$jsonResponse = $response.Content | ConvertFrom-Json
$jsonResponse
```


### Contributing
Contributions to the Face Emotion Analyzer are welcome. Please feel free to submit issues and pull requests.
