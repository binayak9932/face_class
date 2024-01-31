from flask import Flask, request, jsonify
from deepface import DeepFace
import cv2
import numpy as np
import os

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze_image():
    # Check if the post request has the file part
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if file:
        # Save the file temporarily
        filename = "temp.jpg"
        file.save(filename)

        try:
            # Perform facial attribute analysis
            analysis = DeepFace.analyze(img_path=filename, actions=['age', 'gender', 'emotion'])
            # Clean up the saved file
            os.remove(filename)
            return jsonify(analysis)
        except Exception as e:
            return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run( debug=True,use_reloader=False)