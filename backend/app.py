from flask import Flask, request, jsonify
from flask_cors import CORS
from chat_handler import process_chat
from pdf_utils import load_pdf_embeddings

app = Flask(__name__)
CORS(app)

# In-memory vectorstore to simulate database
vectorstore = None

@app.route("/upload_pdf", methods=["POST"])
def upload_pdf():
    global vectorstore
    file = request.files['file']
    if not file:
        return jsonify({"error": "No file uploaded"}), 400
    vectorstore = load_pdf_embeddings(file)
    return jsonify({"message": "PDF processed successfully!"})

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    prompt = data.get("prompt")
    if not prompt:
        return jsonify({"error": "No prompt provided"}), 400
    response = process_chat(prompt, vectorstore)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
