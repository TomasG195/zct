from flask import Flask, render_template, request
from deepface import DeepFace

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyza', methods=['POST'])
def analyza():
    if 'suborx' in request.files:
        obrazok = request.files['suborx']
        obrazok.save('uploaded_image.jpg')  # Uloží nahraný obrázok na server

        # Analýza emocionálneho výrazu z nahraného obrázka
        face_analysis = DeepFace.analyze(img_path="uploaded_image.jpg", enforce_detection=False)

        dominant_emotion = face_analysis[0]["dominant_emotion"]

        return render_template('vysledok.html', dominant_emotion=dominant_emotion)
    return "Nebol zaslaný žiadny súbor."

if __name__ == '__main__':
    app.run(debug=True)
