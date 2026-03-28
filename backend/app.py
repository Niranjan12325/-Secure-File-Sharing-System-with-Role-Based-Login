from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os

app = Flask(__name__)
CORS(app)

# Folder setup
UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), "files")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Dummy users
users = {
    "admin": {"password": "123", "role": "admin"},
    "emp": {"password": "123", "role": "employee"}
}

# File access mapping (who can access which file)
file_access = {}

# AES Key
key = b'Sixteen byte key'

# ---------------- LOGIN ----------------
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data["username"]
    password = data["password"]

    user = users.get(username)

    if user and user["password"] == password:
        return jsonify({
            "role": user["role"],
            "username": username
        })

    return jsonify({"error": "Invalid credentials"}), 401


# ---------------- UPLOAD ----------------
@app.route('/upload', methods=['POST'])
def upload():
    role = request.form.get("role")
    username = request.form.get("username")
    assigned_to = request.form.get("assigned_to")

    if role != "admin":
        return jsonify({"error": "Only admin can upload"}), 403

    file = request.files['file']
    file_data = file.read()

    cipher = AES.new(key, AES.MODE_CBC)
    encrypted = cipher.encrypt(pad(file_data, AES.block_size))

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(filepath, "wb") as f:
        f.write(cipher.iv + encrypted)

    # Assign file to specific user
    file_access[file.filename] = [assigned_to]

    return jsonify({"message": f"File uploaded and assigned to {assigned_to}"})


# ---------------- DOWNLOAD ----------------
@app.route('/download/<filename>', methods=['GET'])
def download(filename):
    role = request.args.get("role")
    username = request.args.get("username")

    # Admin can access all files
    if role == "admin":
        allowed = True
    else:
        allowed = username in file_access.get(filename, [])

    if not allowed:
        return jsonify({"error": "Access denied"}), 403

    filepath = os.path.join(UPLOAD_FOLDER, filename)

    if not os.path.exists(filepath):
        return jsonify({"error": "File not found"}), 404

    with open(filepath, "rb") as f:
        data = f.read()

    iv = data[:16]
    encrypted = data[16:]

    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    decrypted = unpad(cipher.decrypt(encrypted), AES.block_size)

    temp_file = "temp_" + filename
    with open(temp_file, "wb") as f:
        f.write(decrypted)

    return send_file(temp_file, as_attachment=True)


# ---------------- LIST FILES ----------------
@app.route('/files', methods=['GET'])
def list_files():
    return jsonify(os.listdir(UPLOAD_FOLDER))


# ---------------- RUN ----------------
if __name__ == "__main__":
    app.run(debug=True)