import os
import cloudinary
import cloudinary.uploader
import fitz
from dotenv import load_dotenv
from flask import Blueprint, request, jsonify

load_dotenv()

upload_api = Blueprint('upload', __name__)

cloudinary.config(
    cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
    api_key=os.getenv("CLOUDINARY_API_KEY"),
    api_secret=os.getenv("CLOUDINARY_API_SECRET")
)

@upload_api.route('/upload', methods=["POST"])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    file = request.files['file']
    result = cloudinary.uploader.upload(file, resource_type="raw")

    text = ""
    if file.filename.endswith('.pdf'):
        file.seek(0)
        doc = fitz.open(stream=file.read(), filetype="pdf")
        for page in doc:
            text += page.get_text()
    
    return jsonify({
        "url": result['secure_url'],
        "extracted_text": text
    }), 200