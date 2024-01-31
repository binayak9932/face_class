## Installation

Before running the application, you need to install the necessary packages. This can be done via pip:

```bash
pip install requirements.txt
```
## Running the Flask Server
To start the Flask server, run the following command in your terminal:
```bash
python app.py
```

This will start the server on http://127.0.0.1:5000/.


### Sending an Image for Analysis
To analyze an image for emotions, you need to send a POST request to the Flask server. This can be done using PowerShell as follows:

```bash
Invoke-WebRequest -Uri "http://127.0.0.1:5000/predict" -Method Post -Form @{image = Get-Item "C:\path\to\your\image.jpg"}
```
Replace "C:\path\to\your\image.jpg" with the path to the image you want to analyze.



### The  jupyter notebook is named original.ipynb and the dataset has been taken from 
##### ->universe.roboflow.com

## Here are  the Training results

| Epoch | Training Loss | Training Accuracy | Validation Loss | Validation Accuracy |
|-------|---------------|-------------------|-----------------|---------------------|
| 1     | 0.5779        | 69.79%            | 0.5463          | 74.43%              |
| 2     | 0.4424        | 79.61%            | 0.4951          | 78.52%              |
| 3     | 0.4019        | 81.89%            | 0.4026          | 81.62%              |
| 4     | 0.3169        | 86.14%            | 0.3846          | 84.72%              |
| 5     | 0.2591        | 89.05%            | 0.3694          | 83.92%              |
| 6     | 0.2139        | 90.76%            | 0.3517          | 87.61%              |
| 7     | 0.1249        | 94.75%            | 0.4738          | 86.11%              |
| 8     | 0.1210        | 95.66%            | 0.3799          | 88.51%              |
| 9     | 0.0696        | 97.69%            | 0.4243          | 88.61%              |
| 10    | 0.0749        | 97.38%            | 0.4490          | 88.41%              |
| 11    | 0.0479        | 98.49%            | 0.5034          | 88.31%              |
| 12    | 0.0400        | 98.77%            | 0.4283          | 89.91%              |
| 13    | 0.0351        | 98.86%            | 0.4574          | 88.31%              |
| 14    | 0.0328        | 99.12%            | 0.4373          | 89.91%              |
| 15    | 0.0331        | 98.94%            | 0.5053          | 88.91%              |



### Contributing
Contributions  are welcome. Please feel free to submit issues and pull requests.